/**
 * @author Harsh Manocha
 * IIIT-Delhi, B.Tech. (CSE) 2nd year
 */

#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stack>
#include<queue>
#include<stdio.h>
#include<functional>
#include<numeric>

using namespace std;

// Input macros
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define sl(n) scanf("%ld",&n)
#define sf(n) scanf("%f",&n)
#define slf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)

//Output macros
#define pis(n) printf("%d ",n)
#define plfs(n) printf("%lf ",n)
#define plls(n) printf("%lld ",n)
#define pll(n) printf("%lld\n",n)
#define plf(n) printf("%lf\n",n)
#define pi(n) printf("%d\n",n)
#define pl(n) printf("%ld\n",n)
#define pls(n) printf("%ld ",n)
#define pf(n) printf("%f\n",n)
#define pfs(n) printf("%f ",n)

//Some useful shorthands
#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i)
#define REP(i,n) FOR(i,0,n)
#define INF INT_MAX
#define INFL LLONG_MAX
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define IN(a,b) ((b).find(a)!=(b).end())
#define pb push_back
#define sz(x) int(x.size())
#define mp make_pair
#define fill(x,v) memset(x,v,sizeof(x))

#define ll long long int
#define pii pair<int,int>
#define vll vector<long long int>
#define fr first
#define sc second
#define getcx getchar_unlocked

// Some common useful functions
#define MAX(a,b)                     ( (a) > (b) ? (a) : (b))
#define MIN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(ALL(a)); a.erase(unique(ALL(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(ALL(arr),ind)-arr.begin())

#define scan(v,n) vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define mod 1000000007

#define in_type ll //make sure to change the type to use inline fast inp function.


//inline void inp(in_type &n)
//{
//    n=0;
//    in_type ch=getcx();int sign=1;
//    while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
//    while( ch >= '0' && ch <= '9' )
//    n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
//    n=n*sign;
//}


long long int exp_modulo(long long int a,long long int b,long long int c){
    long long int x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c; // squaring the base
        b >>= 1;
    }
    return x%c;
}

/* ******************************************************
Actual Code Starts
****************************************************** */

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	double c,f,x,r,sec;
    for(int T=1;T<=t;T++)
    {
        slf(c);
        slf(f);
        slf(x);
        sec=0.0;
        r=2.0;

        while(true)
        {
            if(x/(r)<(c/(r))+(x/(r+f)))
            {
                break;
            }
            sec+=c/r;
            r+=f;
        }
        printf("Case #%d: %.7lf\n",T,sec+x/r);
    }
	return 0;
}
