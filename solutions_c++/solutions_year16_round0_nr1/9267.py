#include    <iostream>
#include    <stdio.h>
#include    <vector>
#include    <algorithm>
#include    <stack>
#include    <string.h>
#include    <math.h>
#include    <set>
#include    <map>
#include    <utility>

#define     li              long int
#define     ll              long long int
#define     vi              vector<int>
#define     vii             vector<pair<int,int> >
#define     pii             pair<int,int>
#define     vl              vector<ll>
#define     vll             vector<pair<ll,ll> >
#define     pll             pair<ll,ll>
#define     pli             pair<ll,int>
#define     mp              make_pair
#define     TC()            int t;scanf("%d",&t);while(t--)
#define     REP(i,a,b)      for(i=a;i<b;i++)
#define     REPREV(i,b,a)   for(i=b;i>=a;i--)
#define     INP(x)          scanf("%d",&x)
#define     OUT(x)          printf("%d\n",x)
#define     INPLL(x)        scanf("%lld",&x)
#define     OUTLL(x)        printf("%lld\n",x)
#define     INPS(x)         scanf("%s",x)
#define     OUTS(x)         printf("%s\n",x)
#define     trace1(x)       cout <<#x<<" = "<<x<<endl;
#define     trace2(x, y)    cout <<#x<<" = "<<x<<" & "<<#y<<" = "<<y<< endl;
#define     ENDL            printf("\n")
#define     MOD             1000000007
#define     N               100005

using namespace std;

bool AllDigitsSeen(int a[])
{
    int i;
    bool flag=true;
    REP(i,0,10)
    {
        if(a[i]==0)
        {
            flag=false;break;
        }
    }
    return flag;
}
int main()
{
	int n,i,x,ans,given,temp,lol=1,a[20];
	TC()
	{
	    x=2;
	    ans=0;
	    REP(i,0,20)
            a[i]=0;
	    cin>>n;
	    given=n;
	    if(n==0)
            ans=0;
        else
	    {
	        while(1)
            {
                if(AllDigitsSeen(a))
                    break;
                else
                {
                    //ans++;
                    while(n)
                    {
                        //ans++;
                        a[n%10]++;
                        n/=10;
                    }
                    n=given*(x++);
                }
            }
            ans=n-given;
	    }
        if(ans)
            cout<<"Case #"<<lol++<<": "<<ans<<endl;
        else
            cout<<"Case #"<<lol++<<": INSOMNIA"<<endl;
	}
	return 0;
}
