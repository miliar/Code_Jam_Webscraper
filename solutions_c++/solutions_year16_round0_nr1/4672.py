#include<iostream>
#include<stack>
#include<map>
#include<vector>
#include<queue>
#include<set>
#include<algorithm>
#include<string>
#include<iomanip>
#include<stdio.h>
#include<math.h>
#include<ctype.h>
#include<string.h>
#include<cstring>
#include<time.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define pll pair<ll,ll>
#define ppll pair<ll, pair<ll,ll> >
#define inf 1000000007

int main()
{
    ll t,n,flag,temp,j,k,i;
    vector<bool> dig;
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%lld",&n);
        if(!n)
        {
            printf("Case #%lld: INSOMNIA\n",j);
            continue;
        }
        
        dig.resize(10,false);
        flag=0;
        temp=n;
        while(temp)
        {
            dig[temp%10]=true;
            temp/=10;
        }
        i=2;
        
        while(!flag)
        {
            temp=n*i;
            while(temp)
            {
                dig[temp%10]=true;
                temp/=10;
            }
            flag=1;
            for(k=0;k<10;k++)
            {
                if(dig[k]==false)
                {
                    flag=0;
                    break;
                }
            }
            i++;
        }
        printf("Case #%lld: %lld\n",j,n*(i-1));
        dig.clear();
    }
}




