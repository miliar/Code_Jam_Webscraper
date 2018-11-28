#include<stdio.h>
int A[5][5],B[5][5];
int St[30],En[20];
int main()
{
    int T,t,i,j,S,E,x;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&S);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++) scanf("%d",&A[i][j]),St[A[i][j]]=i;
        }
        scanf("%d",&E);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++) scanf("%d",&B[i][j]),En[B[i][j]]=i;
        }
        int cnt=0;
        for(i=1;i<=16;i++)
        {
            if(St[i]==S&&En[i]==E)
            {
                cnt++;
                x=i;
            }
        }
        printf("Case #%d: ",t);
        if(cnt==0) printf("Volunteer cheated!");
        else if(cnt>1) printf("Bad magician!");
        else printf("%d",x);
        printf("\n");
    }
}
