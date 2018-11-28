#include <stdio.h>

int main()
{
    int I,T,a,b,k,i,j,ans;
    scanf("%d",&T);
    for(I=1;I<=T;I++)
    {
        ans = 0;
        scanf("%d %d %d",&a,&b,&k);
        //printf("a = %d,  b = %d, k = %d\n",a,b,k);
        for(i=0;i<a;i++)
            for(j=0;j<b;j++)
                if((i&j)<k)
                {
                    ans++;
          //          printf("%d & %d = %d \n",i,j,i&j);
                }
        printf("Case #%d: %d\n",I,ans);
    }
    return 0;
}
