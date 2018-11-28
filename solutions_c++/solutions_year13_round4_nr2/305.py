#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long LL;
LL l[100],r[100],num[100];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        memset(l,0,sizeof(l));
        memset(r,0,sizeof(r));
        memset(num,0,sizeof(num));
        int n;
        LL p;
        scanf("%d%I64d",&n,&p);
        printf("Case #%d: ",ii);
        if (n==1)
        {
            if (p==1) puts("0 0");
            else puts("1 1");
            continue;
        }
        l[0]=r[0]=0;
        num[0]=1;
        LL tot=(1LL<<(n-1));
        for (int i=1;i<n;i++)
        {
            num[i]=num[i-1]*2;
            r[i]=r[i-1]+tot;
            tot/=2;
        }
        num[n]=num[n-1]+1;
        l[n]=2;
        r[n]=r[n-1];
        tot=(1LL<<(n-2));
        LL tot2=4;
        for (int i=n+1;i<2*n;i++)
        {
            num[i]=num[i-1]+tot;
            l[i]=l[i-1]+tot2;
            r[i]=r[i-1];
            tot2*=2;
            tot/=2;
        }
        l[2*n-1]=r[2*n-1]=(1LL<<n)-1;
        num[2*n]=(1LL<<n)+1;
        for (int i=0;i<2*n;i++)
            if (p>=num[i]&&p<num[i+1]) printf("%I64d %I64d\n",l[i],r[i]);
    }
    return 0;
}

