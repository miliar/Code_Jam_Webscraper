#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
#define MOD 1000002013

using namespace std;

#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define sc(n)                   {char temp[4]; ss(temp); n=temp[0];}
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define MAX(a,b)				((a)>(b)?(a):(b))
#define MIN(a,b)				((a)<(b)?(a):(b))
#define ABS(x)					((x)<0?-(x):(x))
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp						make_pair
#define FF						first
#define SS						second
#define tri(a,b,c)				mp(a,mp(b,c))
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back
#define fill(a,v) 				memset(a,v,sizeof a)
#define all(x)					x.begin(),x.end()
#define SZ(v)					((int)(v.size()))
#define DREP(a)					sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())
#define F(i,m,n)                for(i=m;i<n;i++)
#define FFn(i,n,m)               for(i=n;i>=m;i--)

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<TRI> VT;

int compare(int a,int b)
{
    return(a>b);
}

int main()
{
    FILE *fin=fopen("A-small-attempt2.in","r");
    FILE *fout=fopen("output.txt","w");

    int i,m,n,x,t,a,b,p,j,k,count=0;
    long long c;
    fscanf(fin,"%d",&t);
    for(x=1;x<=t;x++)
    {
        c=0;
        count=0;
        fscanf(fin,"%d %d",&n,&m);
        VI st;VI end;
        for(i=0;i<m;i++)
        {
            fscanf(fin,"%d%d%d",&a,&b,&p);
            c+=(LL((b-a-1)*(b-a)*p)/2);
            for(k=0;k<p;k++)
            {
                st.pb(a);end.pb(b);
                count++;
            }
        }

        long long int newc=0;
        sort(all(st));
        sort(all(end));

        j=0;k=0;
        VI visited(count,0);
        while(j<count)
        {
            if(st[j]<=end[k])
            {
                j++;
            }
            else
            {
                for(i=j-1;i>=0;i--)
                {
                    if(visited[i]==0)
                    break;
                }
                visited[i]=1;
                newc+=(LL((end[k]-st[i]-1)*(end[k]-st[i]))/2);
                k++;
            }
        }
        i=count-1;
        while(k<count)
        {
            while(visited[i])
            i--;
            visited[i]=1;
            newc+=(LL((end[k]-st[i]-1)*(end[k]-st[i]))/2);
            k++;
        }
        int ans;
        ans=int((newc-c)%MOD);
        fprintf(fout,"Case #%d: %d\n",x,ans);
    }
    return(0);

}
