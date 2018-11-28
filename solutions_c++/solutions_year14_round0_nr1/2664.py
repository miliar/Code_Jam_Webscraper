#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define MST(a,b) memset(a,b,sizeof(a))

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int nn;
    int a[17],ans[17];
    scanf("%d",&nn);
    FOR(ii,1,nn)
    {
        printf("Case #%d: ",ii);
        MST(a,0);
        int r1,r2;
        scanf("%d",&r1);
        FOR(i,1,4)
        FOR(j,1,4)
        {
            int x;
            scanf("%d",&x);
            if(i==r1)a[x]++;
        }
        scanf("%d",&r2);
        FOR(i,1,4)
        FOR(j,1,4)
        {
            int x;
            scanf("%d",&x);
            if(i==r2)a[x]++;
        }
        int ansn=0;
        FOR(i,1,16)if(a[i]==2)ansn++;
        if(ansn==0)printf("Volunteer cheated!\n");
        if(ansn==1)FOR(i,1,16)if(a[i]==2)printf("%d\n",i);
        if(ansn>1)printf("Bad magician!\n");
    }
    return 0;
}
