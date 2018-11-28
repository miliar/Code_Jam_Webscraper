#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
  //#include<iostream>
#include<algorithm>
   #include<fstream>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
#include <ctime>
using namespace std;

//#define s(n)					scanf("%d",&n)
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
#define sz(v)					((int)(v.size()))
#define DREP(a)					sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())
#define forall(i,m,n)                for(i=m;i<n;i++)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pii> tri;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<tri> vt;
typedef vector< string > vs;
int compare(int a,int b)
{
    return(a>b);
}
ifstream cin("A-small-attempt0.in");
ofstream cout("output.out");
int main()
{
    int a,b,k,i,j;
    int t;
    cin>>t;
    for(int ts=1;ts<=t;ts++)
    {
        int n;
        cin>>n;
        vs a(n);
        for(i=0;i<n;i++)
        {
            cin>>a[i];

        }
        vs s(n);
        vector< vi > ref(n);
        for(i=0;i<n;i++)
        {
            s[i].pb(a[i][0]);
            ref[i].pb(1);
            for(j=1;j<sz(a[i]);)
            {
                if(a[i][j]==s[i][sz(s[i])-1])
                {
                    j++;
                    ref[i][sz(ref[i])-1]++;
                }
                else
                {
                    s[i].pb(a[i][j]);
                    ref[i].pb(1);
                    j++;
                }
            }
        }
        int f=1;
        for(i=0;i<n-1;i++)
        {
            if(s[i]!=s[i+1])
            {
                f=0;

                break;
            }
        }
        if(f==0)
        {
            cout<<"Case #"<<ts<<": "<<"Fegla Won\n";
        }
        else
        {
            int c=0;
            for(j=0;j<sz(s[0]);j++)
            {

                int minv=101;
                int maxv=0;
                for(i=0;i<n;i++)
                {
                    minv= min(minv,ref[i][j]);
                }
                for(i=0;i<n;i++)
                {

                    maxv= max(maxv,ref[i][j]);
                }
                int minins=101;
                for(k=minv;k<=maxv;k++)
                {
                    int mink=0;
                    for(i=0;i<n;i++)
                    {
                        mink+= abs(ref[i][j]-k);
                    }
                    minins= min(mink, minins);
                }
                c+=minins;

            }
            cout<<"Case #"<<ts<<": "<<c<<"\n";

        }
    }
    return 0;


}
