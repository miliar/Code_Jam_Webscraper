#include<cstdio>
#include<iostream>
int main()
{
    int t,n1,n2,mat1[4][4],mat2[4][4],ans,count,i,j,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
    	count =0;
        scanf("%d",&n1);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&mat1[i][j]);
            }
            //printf("\n");
        }
        scanf("%d",&n2);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&mat2[i][j]);
            }
           // printf("\n");
        }
        //count = 0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                //printf("%d %d",mat1[n1-1][i],mat2[n2-1][j]);
                if(mat1[n1-1][i] == mat2[n2-1][j])
                {
                    count++;
                    ans = mat1[n1-1][i];
                }
				//printf("\n");
            }
        }
        //printf("%d %d %d",count,n1,n2);
        if(count == 1)
            printf("Case #%d: %d\n",k,ans);
        else if(count == 0)
            printf("Case #%d: Volunteer cheated!\n",k);
        else
            printf("Case #%d: Bad magician!\n",k);
    }
    return 0;
}
