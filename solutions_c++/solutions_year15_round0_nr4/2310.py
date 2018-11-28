//Abinash Ghosh(Om)
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <climits>
#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <sstream>
#include <algorithm>
#include <ctime>
#include <cassert>
using  namespace  std;

#define PI acos(-1.0)
#define MAX 10000007
#define EPS 1e-9
#define mem(a,b) memset(a,b,sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define Sort(x) sort(x.begin(),x.end())
#define FOR(i, b, e) for(int i = b; i <= e; i++)
#define FORR(i, b, e) for(int i = b; i >= e; i--)
#define pr(x) cout<<x<<"\n"
#define pr2(x,y) cout<<x<<" "<<y<<"\n"
#define pr3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n";
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

typedef  long long ll;
typedef  pair <int, int> pii;
typedef  pair <double , double> pdd;
typedef  pair <ll , ll > pll;
typedef  vector <int> vi;
typedef  vector <pii> vpii;
typedef  vector <ll > vl;
//ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
//ll powmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};
//int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};
//int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction

int main()
{
    READ("D-small-attempt1.in");
    WRITE("out.out");
        int T,x,r,c;
//    int cnt=0;
//    FOR(i,1,4)
//    {
//        FOR(j,1,4)
//        {
//            FOR(k,j,4){
//            printf("%d %d %d\n",i,j,k);
//            cnt++;
//            }
//        }
//    }
//    pr(cnt);
    scanf("%d",&T);
    FOR(t,1,T)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(r>c)swap(r,c);
        int ans;
        if(x==4)
        {
            if((r==4&&c==4)||(r==3&&c==4))
            ans=2;
            else
            ans=1;
        }
        else if(x==3)
        {
            if((r==2&&c==3)||(r==3&&c==3)||(r==3&&c==4))
                ans=2;
            else ans=1;
        }
        else if(x==2)
        {
            if((r*c)%2==0)ans=2;
            else ans=1;
        }
        else ans=2;
        if(ans==1)
        printf("Case #%d: RICHARD\n",t);
        else
        printf("Case #%d: GABRIEL\n",t);
    }
    return 0;
}


