/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long
#define M 1000000007
ll vs[1000];
ll E,R,N;

ll dp(ll pos,ll en)
{
    if(pos>N)return 0;
    ll ret=0;
    for(int i=0;i<=en;i++)
    {
        ret=max(ret,i*vs[pos]+( dp( pos+1,min(E,en-i+R) ) ) );
    }
    return ret;
}

int main()
{
    #ifndef ONLINE_JUDGE
	in("in.txt");
	out("out.txt");
    #endif

    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        cin>>E>>R>>N;
        for(int i=1;i<=N;i++)
            cin>>vs[i];
        printf("Case #%d: ",caseno++);
        cout<<dp(1,E)<<endl;
    }
	return 0;
}
