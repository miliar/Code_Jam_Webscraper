#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long ll;

vector<ll> sp;
bool parimdom(ll no)
{
    char str[200];
    sprintf(str,"%I64d",no);
    int nlen=strlen(str),i;
    int n=nlen/2;
    for(i=0;i<n;i++)
    {
        if(str[i]!=str[nlen-1-i]) return 0;
    }
    return 1;
}
void pre()
{
    ll i,n;
    for(i=1;i<=10000000;i++)
    {
        if(parimdom(i))
        {
            n=i*i;
            if(parimdom(n))
            {
                //printf("%I64d %I64d\n",i,n);
                sp.push_back(n);
            }
        }
    }
}


int main()
{
    int t,C=1;
    freopen("C-large-1.in","r",stdin);
    freopen("out.txt","w",stdout);
    pre();
    ll a,b;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%I64d %I64d",&a,&b);
        int lo=(int)(lower_bound(sp.begin(),sp.end(),a)-sp.begin());
        int up=(int)(lower_bound(sp.begin(),sp.end(),b)-sp.begin());
        if(sp[up]==b)
            printf("Case #%d: %d\n",C++,up-lo+1);
        else
            printf("Case #%d: %d\n",C++,up-lo);
    }
    return 0;
}
