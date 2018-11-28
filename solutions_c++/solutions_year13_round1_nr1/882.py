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


int main()
{
    #ifndef ONLINE_JUDGE
	in("in.txt");
	out("out.txt");
    #endif

    int cs,caseno=1;
    cin>>cs;
    while(cs--)
    {
        ll t,r;
        cin>>r>>t;
//        cout<<r<<" "<<t<<endl;
        ll cnt=0;
        while(t>0)
        {
            ll area=(r+1)*(r+1)-r*r;
//            cout<<area<<" "<<t<<endl;
            if(area>t)break;
            t-=area;
            cnt++;
            r+=2;
        }
        printf("Case #%d: %lld\n",caseno++,cnt);
    }
	return 0;
}
