#include<iostream>
#include<vector>
#include<string.h>
#include<set>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
typedef long long int ll;
int main()
{
   int t,i,j,k,x,y;
   //ios::sync_with_stdio(false);
    string ans;
    freopen("b.in","r",stdin);
   freopen("b2.out","w",stdout);
    int test=1;
    cin>>t;
    while(t--)
    {
        ans="";
        cin>>x>>y;
        if(x>=0 && y>=0)
        {
            while(x--)
            {
                ans+="WE";
            }
            while(y--)
            {
                ans+="SN";
            }

        }
        else if(x<=0 && y>=0)
        {
            x=abs(x);
            while(x--)
            {
                ans+="EW";
            }
            while(y--)
            {
                ans+="SN";
            }
        }
        else if(x<=0 && y<=0)
        {
            x=abs(x);
            while(x--)
            {
                ans+="EW";
            }
            y=abs(y);
            while(y--)
            {
                ans+="NS";
            }
        }
        else if(x>=0 && y<=0)
        {
            while(x--)
            {
                ans+="WE";
            }
            y=abs(y);
            while(y--)
            {
                ans+="NS";
            }
        }
        cout<<"Case #"<<test++<<": "<<ans<<endl;
    }
    return 0;
}
