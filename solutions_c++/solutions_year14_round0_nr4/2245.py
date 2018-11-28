#include<iostream>
#include<cstdio>
#include<algorithm>
#include<memory.h>
#include<vector>
#include<stack>
#include<queue>
#include<cassert>
#include<cstdlib>
#include<cmath>
#include<map>
#include<utility>
#include<cstring>

#define DEBUG(x) cout<<#x<<"= "<<x<<endl
#define DEBUGARR(x,i,f) for(int iter = i; iter <= f; ++iter) printf("%s[%d]=%d\n",#x, iter, x[iter])
#define MAX(a,b) ((a)>(b))? (a):(b)
#define MAX3(a,b,c) MAX(a,MAX(b,c))
#define MIN(a,b) ((a)<(b))? (a):(b)
#define MIN3(a,b,c) MIN(a,MIN(b,c))
#define bit(n,i) (n&(1<<(i-1)))
#define setbit(n,i) n |= (1<<(i-1))
#define inf (1<<30)
#define SETZERO(x) memset( x, 0, sizeof(x))
#define SETMIN1(x) memset( x, -1, sizeof(x))
#define CLEAR(x) while(!x.empty()) x.pop();
#define FOR(i,in,fin) for( i = (in); i <= (fin); ++i)
#define FORL(i,in,fin) for( i = (in); i < (fin); ++i)
#define FORD(i,in,fin) for( i = (in); i >= (fin); --i)
#define INC(a,b,c) ((a)<=(b) && (b)<=(c))
#define pb push_back
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d\n",x)
#define sll(x) scanf("%lld",&x)
#define pll(x) printf("%lld\n",x)
#define sortv(v) sort(v.begin(),v.end())
#define sortar(a,i,n) sort(a+i,a+i+n)
#define findmp(mp,x) (mp.find(x)!=mp.end())
typedef long long ill;
using namespace std;
typedef pair <int,int> pii;
const int mod = 1000000007;
//code begins here
int main()
{
    #ifndef ONLINE_JUDGE
        freopen( "a.in", "r", stdin);
        freopen("a.out","w",stdout);
    #endif
    int t,test_case;
    scanf("%d",&t);
    FOR(test_case,1,t)
    {
        printf("Case #%d: ",test_case);
        int n,i;
        si(n);
        double a1[1001],a2[1001];
        map <double,int> mp;
        mp.clear();
        int l1=1,r1=n,l2=1,r2=n,ans1=0,ans2=0;
        FOR(i,1,n)
            scanf("%lf",&a1[i]);
        FOR(i,1,n)
            scanf("%lf",&a2[i]),mp[a2[i]]=1;
        sort(a1+1,a1+1+n);
        sort(a2+1,a2+1+n);
        FOR(i,1,n){
            map <double,int>::iterator it;
            mp[a1[i]]=1;
            it = mp.find(a1[i]);
            it++;
            if(it==mp.end())
                ans2++;
            else
                mp.erase(it);
            mp.erase(a1[i]);
        }
        while(l1<=r1){
            if(a1[r1]<a2[r2]){
                l1++,r2--;
            }
            else{
                ans1++,r1--,r2--;
            }
        }
        printf("%d %d\n",ans1,ans2);
    }
    //DEBUG(amx);
}


