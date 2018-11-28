#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>

#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
#include<fstream>
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
#define forall(i,m,n)                for(i=m;i<n;i++)

typedef long long ll;
typedef double dd;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pii> tri;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<dd> vd;
typedef vector<pii> vii;
typedef vector<tri> vt;

int compare(dd a,dd b)
{
    return(a<b);
}
ifstream cin("D-large.in");
ofstream cout("output.out");
int main()
{
    int t,i,j,pn1,pn2;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int n;
        cin>>n;
        vd na(n),ke(n);
        for(i=0;i<n;i++)
        {
            cin>>na[i];
        }
        for(i=0;i<n;i++)
        {
            cin>>ke[i];
        }
        for(i=0;i<n;i++)
        {
            int a;
        }
        sort(all(na));
        sort(all(ke));
        for(i=0;i<n;i++)
        {
            int a;
        }
         i=0,j=0,pn1=0;
        while(i!=n&&j!=n)
        {
            if(na[i]>ke[j])
            {
                j++;
            }
            else
            {
                i++;j++;
            }
        }
        pn1+= (n-i);
         i=0;
          pn2=0;
          int x=0;
          int y=n-1;
         while(i!=n )
         {
             if(na[i]<ke[x])
             {
                 i++;
                 y--;
             }
             else
             {
                 i++;
                 x++;
                 pn2++;
             }
         }
            cout<<"Case #"<<tt<<": "<<pn2<<" "<<pn1<<"\n";
            for(i=0;i<n;i++)
            {
                vi b(n+1);
                b[i]=0;
            }
    }


    return 0;
}
