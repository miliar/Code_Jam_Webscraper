#include<cstdio>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<math.h>
#include<iostream>
#include<ctype.h>
#define ll long long
using namespace std;
double pi=acos(-1.0);
int ok[1005],tmp[100];
bool pal(int x)
{
    int l=0,j;
    while(x>0)
    {
        tmp[l++]=x%10;
        x/=10;
    }
    if(l==1) return true;
    else
    {
        if(l%2==1)
        {
            j=l/2;
            for(int i=0;j+i<l&&j-i>=0;i++)
                if(tmp[i+j]!=tmp[j-i]) return false;
        }
        else
        {
            j=l/2-1;
            for(int i=0;i+j+1<l&&j-i>=0;i++)
                if(tmp[i+j+1]!=tmp[j-i]) return false;
        }
        return true;
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int cas,cnt,k=1,a,b;
    for(int i=1;i*i<=1005;i++)
    {
        if(pal(i*i)&&pal(i)) ok[i*i]=1;
    }
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d %d",&a,&b);
        cnt=0;
        for(int i=a;i<=b;i++)
            if(ok[i]==1) cnt++;
        printf("Case #%d: %d\n",k++,cnt);
    }
    return 0;
}
