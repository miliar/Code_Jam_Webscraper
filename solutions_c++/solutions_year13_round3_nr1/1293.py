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

    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        string a;
        int d;
        cin>>a>>d;
        int res=0;
        int n=a.size();
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                int cnt=0;
                int ar[1000];
                memset(ar,0,sizeof(ar));
                for(int st=i;st<=j;st++)
                {
                    if(a[st]!='a' && a[st]!='e' && a[st]!='i' && a[st]!='o' && a[st]!='u')
                    {
                        if(st==0)ar[st]=1;
                        else
                        ar[st]=ar[st-1]+1;
                    }
                }
                for(int st=i;st<=j;st++)
                {
                    if(ar[st]>=d)
                    {
//                        cout<<i<<" "<<j<<endl;
                        res++;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",caseno++,res);
    }
	return 0;
}
