
/*
Author : Vivek Hamirwasia

A programmer started to cuss,
Because getting to sleep was a fuss.
As he lay there in bed,
Looping 'round in his head,
Was: while(!asleep()) sheep++;

 */
#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstdlib>
#include<climits>
#include<cstring>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LLD long long
#define VI vector < int >
#define PII pair < int , int >

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf("%s",x)

#define pis(x) printf("%d ",x)
#define pls(x) printf("%lld ",x)
#define pin(x) printf("%d\n",x)
#define pln(x) printf("%lld\n",x)
#define pds(x) printf("%.12f ",x)
#define pdn(x) printf("%.12f\n",x)
#define pnl() printf("\n")
#define MAX 1000000000
long double C,F,X;
long double solve()
{
    long double cur = 2.0;
    long double z = 0;

    long double ans = X/cur;
    for(int i=0;i<=100000;i++)
    {
	z += C/cur;
	cur += F;
	ans = min(ans, z+X/cur);
    }
    return ans;
}
int main()
{
    int t;
    cin>>t;
    for(int kase=1;kase<=t;kase++)
    {
	cin>>C>>F>>X;
	printf("Case #%d: %.7Lf\n",kase,solve());
    }
   

    return 0;
}
