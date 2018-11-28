#include <stdio.h>

int a[100000];

void solve()
{
    int smax;
    scanf("%d",&smax);
    getchar();

    
    for (int i=0;i<=smax;i++) a[i] = getchar() - '0';
    //for (int i=0;i<smax;i++) printf("%d<----\n",a[i]);


    int num=a[0];
    int ans = 0;
    for (int i=1;i<=smax;i++)
    {   
        if ( i > num ) ans += i-num, num += i-num;
        num += a[i];
    }
    printf("%d\n",ans);
}



int main()
{
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {

        printf("Case #%d: ",i);
        solve();
    }
    return 0;

}
