#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>
#define forup(i,a,b) for (int i=a;i<=b;i++)
#define fordown(i,a,b) for (int i=a;i>=b;--i)

using namespace std;

int test;
long long n,P;

int main(){
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    scanf("%d",&test);
    forup(uu,1,test)
    {
        printf("Case #%d: ",uu);
        scanf("%I64d%I64d",&n,&P);
        long long now=1LL<<n;
        --now;
        long long sx=now;
        long long step=0,value=0;
        now=P;bool ok=true;
        fordown(j,n-1,0)
        {
            if (now<=1LL<<(long long)j) 
            {
                printf("%I64d ",step);
                ok=false;
                break;
            }
            else step+=1LL<<(long long)(++value),now-=1LL<<(long long)j;
        }
        if (ok) printf("%I64d ",sx);
        now=P;
        step=(1LL<<n)-1;value=0;
        fordown(j,n,0)
        {
             if (now>=(1LL<<(long long)j)) 
             {
                printf("%I64d\n",step);
                break;
             }
             else step-=(1LL<<(long long)(value++));
        }
    }
}
        
