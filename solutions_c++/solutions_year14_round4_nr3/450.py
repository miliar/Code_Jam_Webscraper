#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<ctime>

using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b)  ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

#define MP make_pair
#define pb push_back
#define inf  1000000000
#define maxn 1000005
#define maxc 100001
#define MP make_pair

typedef long long LL;
typedef pair<int,int> pi;
typedef pair<pi,pi> pii;
//typedef __int64 LL;

struct rect
{
   rect() {}
   rect(LL a,LL b,LL c,LL d) : c1(a), r1(b),c2(c),r2(d) {}
   LL r1,r2,c1,c2;
};

rect rects[1005];
LL R,C;
char grid[2500][2500];
LL cr[2500];

int dc[]={-1,0,+1,0};
int dr[]={0,+1,0,-1};



const int MAXV = 100002, MAXE = 600005, INF = 10000005;
const long  CAPINF = 2*INF;

struct Dinic
{
    int V, source, sink;
    int eind, eadj [MAXE], enext [MAXE], elast [MAXV], start [MAXV];
    int front, back, q [MAXV], dist [MAXV];
    int ecap [MAXE];

    inline void init (int v)
    {
        V = v;
        eind = 0;
        if (V > 0)
			memset (elast, -1, V*sizeof (int));

    }

    inline void addedge (int a, int b, int cap1, int cap2)
    {
        eadj [eind] = b; ecap [eind] = cap1; enext [eind] = elast [a]; elast [a] = eind++;
        eadj [eind] = a; ecap [eind] = cap2; enext [eind] = elast [b]; elast [b] = eind++;
    }

    bool bfs ()
    {
		int i;
        for(i=0;i<=V;i++) dist[i]=INF;
        front = back = 0;
        q [back++] = source; dist [source] = 0;

        while (front < back)
        {
            int top = q [front++];
            for (int i = elast [top]; i != -1; i = enext [i])
				if (ecap [i] > 0 && dist [top] + 1 < dist [eadj [i]])
                {
					dist [eadj [i]] = dist [top] + 1;
                    q [back++] = eadj [i];
                }

        }

        return dist [sink] < INF;
    }

    int dfs (int num, int pcap)
    {
        if (num == sink)
            return pcap;

        int total = 0;

        for (int &i = start [num]; i != -1; i = enext [i])
            if (ecap [i] > 0 && dist [num] + 1 == dist [eadj [i]])
            {
                int p = dfs (eadj [i], MIN (ecap [i], pcap));
                ecap [i] -= p;
                ecap [i ^ 1] += p;
                pcap -= p;
                total += p;

                if (pcap == 0)
                    break;
            }

        return total;
    }

    int flow (int _source, int _sink)
    {
        if (V == 0)
            return -1;

        source = _source; sink = _sink;
        int total = 0;

        while (bfs ())
        {
            memcpy (start, elast, V * sizeof (int));
            total += dfs (source, CAPINF);
        }

        return total;
    }
};


Dinic  graph;

int main()
{
	int i,j,k,tests,cs=0,n;

	freopen("C-small-attempt3.in","r",stdin);
	freopen("C-small-attempt3.out","w",stdout);
	//freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{
	  // scanf("%d%d%d",&C,&R,&n);
      cin>>C>>R>>n;

	   MEM(grid,0);
	   int tot=R*C;

	   int s=0,t=2*R*C+1;

	   for(i=0;i<n;i++)
	   {
	      LL r1,c1,r2,c2;
	      cin>>c1>>r1>>c2>>r2;

         for(k=c1;k<=c2;k++)
            for(j=r1;j<=r2;j++)
                  grid[j][k]=1;
	   }

	   graph.init(2*R*C+2);


	   for(i=0;i<R;i++)
         for(j=0;j<C;j++)
         {
            int id = i*C + j + 1;

            if(grid[i][j]) continue;

           // printf("%d %d\n",i,j);

            if(i==0)
               graph.addedge(s,id,1,0);
            if(i==R-1)
               graph.addedge(id+tot,t,1,0);

            graph.addedge(id,id+tot,1,0);

            for(k=0;k<4;k++)
            {
               int ni=i+dr[k],nj=j+dc[k];
               if(ni<0 || nj<0 || ni>=R || nj>=C || grid[ni][nj]) continue;
               int id2 = ni*C + nj +1;
               graph.addedge(id+tot,id2,1,0);
            }
         }





      //for(i=0;i<R;i++)

	   int ans=graph.flow(s,t);


		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
}
