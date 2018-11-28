/*
Shamim Ehsan
SUST CSE 12
*/
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>
#include<limits.h>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<algorithm>
#include<sstream>
#define PI (2* acos(0))
#define pb push_back
#define ll long long
using namespace std;
//int X[]= {0,0,1,-1};
//int Y[]= {-1,1,0,0};
//int X[]= {0,0,1,1,1,-1,-1,-1};
//int Y[]= {-1,1,0,1,-1,0,1,-1};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("newoutput.txt","w",stdout);

    ll  int t,n,temp,ans;
    scanf("%lld",&t);
    for(int cs=1;cs<=t;cs++)
    {
        scanf("%lld",&n);
        bool flag[20];
        memset(flag, 0 ,sizeof flag);
        if(n)
        {
                for(int i=1;i<1000000;i++)
        {
           temp= n*i;
            while(temp)
            {
                flag[temp%10]= true;
                temp/=10;
            }
            int ct=0;
        for(int j=0;j<=9;j++)
        {
            if(flag[j])
                ct++;
        }
        if(ct==10)
        {
            ans= n*i;
            break;
        }
        if(i==99999)
            ans=-1;
        }
        }
        else
            ans =-1;


    if(ans==-1)
        printf("Case #%d: INSOMNIA\n",cs);
    else
        printf("Case #%d: %lld\n",cs,ans);

    }

    return 0;
}

