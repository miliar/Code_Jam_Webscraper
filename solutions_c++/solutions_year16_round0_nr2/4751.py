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

void flip(char *s, ll ind)
{
    char temp;
    ll i=0,j=ind;
    while(i<=j)
    {
        temp=s[i];
        if(s[j]=='+')
            s[i]='-';
        else
            s[i]='+';
        if(temp=='+')
            s[j]='-';
        else
            s[j]='+';
        i++;
        j--;
    }
}

ll pancake(char *s, ll n, char side)
{
    if(n==0)// only one pancake
    {
        if(s[n]==side)
            return 0;
        else
            return 1;
    }
    
    if(s[n]==side)
        return pancake(s,n-1,side);
    
    if(s[n]==s[0])
    {
        flip(s,n);
        return 1+pancake(s,n-1,side);
    }
    if(side=='+')
        side='-';
    else
        side='+';
    return 1+pancake(s,n-1,side);
}

int main()
{
    ll t,i;
    char s[105];
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%s",s);
        printf("Case #%lld: %lld\n",i,pancake(s,strlen(s)-1,'+'));
    }
}




