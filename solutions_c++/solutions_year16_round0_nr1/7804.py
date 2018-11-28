#include <iostream>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <math.h>
#include <stack>
#include <queue>
#include <ctype.h>
#include <map>
#include <bitset>
#include <limits>
typedef long long ll;
#define filla(x,y) memset(x,y,sizeof(x))
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
#define F first
#define S second
#define MOD 1000000007
using namespace std;
/*long long choose(int n,int k)
{
    if(k==0)
        return 1;
    else
    {
        long long f=1;
        if(k>n-k)
            k=n-k;
        int p=1;
        while(p<=k)
        {
            f*=n--;
            f/=p++;
        }
        return f;
    }
}
ll power(int a,int b)
{
    ll ret;
    if(b==0)
        return 1;
    if(b==1)
        return a;
    ret=power(a,b/2);
    ret=(ret*ret);
    if(b&1)
        ret=(ret*a);
    return ret;
}
bool cmp(int a,int b)
{
    return a>b;
}*/
int main()
{
    freopen("in1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int z;
    for(z=1;z<=t;z++)
    {
        ll n;
        int a[10],i;
        for(i=0;i<10;i++)
            a[i]=0;
        scanf("%lld",&n);
        if(n==0)
            printf("Case #%d: INSOMNIA\n",z);
        else
        {
            ll p,j,ctr=0,ctr1=0,k=1;
            while(ctr1<10)
            {
                p=n;
                p=p*k;
                k++;
                j=p;
                while(p>0)
                {
                    int l=p%10;
                    if(a[l]==0)
                    {
                        a[l]=1;
                        ctr1++;
                    }
                    p=p/10;
                }
            }
            printf("Case #%d: %d\n",z,j);
        }
    }
    return 0;
}
