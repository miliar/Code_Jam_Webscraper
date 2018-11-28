#include<cstdio>
#include<cstdlib>

int arr[5][5],arr1[5][5];


int main()
{
    //freopen("out.txt","w",stdout);
    int t,r1,i,j,c,ans,r2,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        c=0;
        scanf("%d",&r1);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                scanf("%d",&arr[i][j]);
        }
        scanf("%d",&r2);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                scanf("%d",&arr1[i][j]);
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(arr[r1][i]==arr1[r2][j])
                    {
                        c++;
                        ans=arr[r1][i];
                    }
            }
        }
        if(c==1)
            printf("Case #%d: %d\n",k,ans);
        else if(c==0)
            printf("Case #%d: Volunteer cheated!\n",k);
        else printf("Case #%d: Bad magician!\n",k);
    }

    return 0;
   // fclose(stdout);
}
