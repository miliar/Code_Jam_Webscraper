#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <ctime>
#define mod 1000000007
#define INF 10000
using namespace std;

long long num[20];

bool check(long long x)
{
    int tot=0,i;
    while(x)
    {
        num[++tot]=x%10;
        x/=10;
    }
    for(i=1;i<=tot/2;i++)
    {
        if(num[i]!=num[tot-i+1])
            return false;
    }
    return true;
}

long long ans[50];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long i,A,B;
    int k=0;
    for(i=1;i<=10000000;i++)
    {
        if(check(i)&&check(i*i))
            ans[++k]=i*i;
    }
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int now=0;
        scanf("%lld%lld",&A,&B);
        for(i=1;i<=k;i++)
        {
            if(ans[i]>B)
                break;
            if(ans[i]>=A)
                now++;
        }
        printf("Case #%d: %d\n",++cas,now);
    }
    return 0;
}
