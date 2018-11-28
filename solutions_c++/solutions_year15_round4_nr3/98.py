#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define maxn 6000

#define INF 1000000000

struct edge
{
        int id, wg, anti;
        edge() {}
        edge(int id, int wg, int anti): id(id), wg(wg), anti(anti) {}
};

vector<edge> e[maxn];

void addedge(int x, int y, int z)
{
        //cout<<x<<" "<<y<<" "<<z<<endl;
        e[x].push_back(edge(y,z,e[y].size()));
        e[y].push_back(edge(x,0,e[x].size()-1));
}

int source, sink, flow, augc, found;
int h[maxn], vh[maxn], cur[maxn];

void sap(int m)
{
        if (m==sink)
        {
                found=1; flow+=augc;
                return;
        }

        int augc2=augc;
        vector<edge>::iterator it=e[m].begin()+cur[m];
        while (it<e[m].end())
        {
                if (it->wg && h[m]==h[it->id]+1)
                {
                        cur[m]=it-e[m].begin();
                        augc=min(augc,it->wg);
                        sap(it->id);
                        if (found) break;
                        if (h[source]>=sink) return;
                        augc=augc2;
                }
                it++;
        }

        if (found)
        {
                it->wg-=augc;
                e[it->id][it->anti].wg+=augc;
        }
        else
        {
                int minh=sink-1, minhi=0;
                rept(it,e[m])
                        if (it->wg && h[it->id]<minh)
                        {
                                minh=h[it->id]; minhi=it-e[m].begin();
                        }
                vh[h[m]]--; if (vh[h[m]]==0) h[source]=sink;
                h[m]=minh+1;
                vh[h[m]]++;
                cur[m]=minhi;
        }
}

void networkflow()
{
        flow=0; memset(h,0,sizeof h); 
        memset(vh,0,sizeof vh); vh[0]=sink;
        memset(cur,0,sizeof cur);
        while (h[source]<sink)
        {
                augc=0x7fffffff; found=0;
                sap(source);
        }
}

char buf[100010];
vector<string> lis[maxn];

void lemon()
{
	int n; scanf("%d",&n); cin.getline(buf,99990); 
	rep(i,1,n) lis[i].clear();
	rep(i,1,n)
	{
		cin.getline(buf,99990); string s=buf; s+=" ";
		string t="";
		rep(j,0,int(s.length())-1)
		{
			if (s[j]==' ') 
			{
				if (t!="") lis[i].push_back(t);
				t="";
			}
			else  t+=s[j];
		}
	}
	map<string, vector<int> > oc;
	rep(i,1,n) rept(it,lis[i]) oc[*it].push_back(i);

	source=n+oc.size()*2+1; sink=source+1;
	int all=n;
	rep(i,1,sink) e[i].clear();
	addedge(source,1,INF);
	addedge(2,sink,INF);
	rept(it,oc)
	{
		all++;
		rept(it2,it->second) addedge(*it2,all,INF);
		addedge(all,all+1,1);
		all++;
		rept(it2,it->second) addedge(all,*it2,INF);
	}
	networkflow();
	printf("%d\n",flow);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("C.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase)
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

