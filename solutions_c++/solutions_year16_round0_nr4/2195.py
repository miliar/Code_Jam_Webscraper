#include <stdio.h>
int main()
{
    int i,j,m,n,t;
    int k,c,s;
    long long pos[150];
   
    scanf("%d",&t);
    for(m=1;m<=t;m++)
    {   
        printf("Case #%d: ",m);
        scanf("%d %d %d",&k,&c,&s);//原始长度，复杂度，可见数
        for(i=1;i<=s;i++)
            printf("%d ",i);
        printf( "\n");
    }



    return 0;
}