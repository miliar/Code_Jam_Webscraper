#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<map>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<map>
#include<sstream>
#define FOR(i, s, e) for(int i=s; i<e; i++)
#define loop(i, n) for(int i=0; i<n; i++)
#define getint(n) scanf("%d", &n)
#define pb(a) push_back(a)
#define ll long long
#define SZ(a) int(a.size())
#define read() freopen("input.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
#define mem(a, v) memset(a, v, sizeof(a))
#define all(v) v.begin(), v.end()
#define pi acos(-1.0)
#define check printf("t\n")
#define mod abs
#define pf(k) printf("%d\n",k)
#define sf(k) scanf("%d",&k)
#define llpf(k)  printf("%lld\n",k)
#define llsf(k) scanf("%lld",&k)
#define double_sf(k,t) scanf("%d %d",&k,&t)
#define double_pf(k,t) printf("%d %d\n",k,t)
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000
using namespace std;
int main()
{

    ios_base::sync_with_stdio(false);
    int i,j,n,m,a[4][4],b[4][4],ans;
    int t,countt=0,t1=1,temp;

	freopen("A-small-attempt3.in", "r", stdin);
    freopen("testO.in", "w", stdout);
    sf(t);
    while(t1<=t)
    {countt=0;
    sf(n);
    loop(i,4)
    {
        loop(j,4)
        sf(a[i][j]);
    }
       sf(m);
    loop(i,4)
    {
        loop(j,4)
        sf(b[i][j]);
    }
   loop(i,4)
   {
       temp=a[n-1][i];
       {

           loop(j,4)
           {
            if(temp==b[m-1][j])
            {
                ans=temp;
                countt++;
            }
           }
       }
   }
   if(countt==0)
  printf ("Case #%d: Volunteer cheated!\n",t1);
  else if(countt==1)
 printf("Case #%d: %d\n",t1,ans);
 else if(countt>1)
 printf("Case #%d: Bad magician!\n",t1);
 t1++;
    }

    return 0;
}
