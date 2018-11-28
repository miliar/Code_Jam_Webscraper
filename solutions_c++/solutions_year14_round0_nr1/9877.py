#include<stdio.h>
#include<string.h>
int main()
{    freopen("E:\\A-small-attempt1.in","r",stdin);
    freopen("E:\\out.txt","w",stdout);
    int x,ans=0;
    scanf("%d",&x);
    int a[4][4],b[4][4];
    while(x--)
    {   ans++;
        int i,j,x1,y1,flag=0,num;
        scanf("%d",&x1);
        x1-=1;
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&y1);
        y1-=1;
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                scanf("%d",&b[i][j]);
        for(i=0;i<4;i++)
         for(j=0;j<4;j++)
            if(a[x1][i]==b[y1][j])
            {num=a[x1][i];
               flag++;}
        if(flag==1)
            printf("Case #%d: %d\n",ans,num);
        else if(flag>1)
                 printf("Case #%d: Bad magician!\n",ans);
        else  printf("Case #%d: Volunteer cheated!\n",ans);

    }
}
