#include<stdio.h>
int main()
{
    FILE *input,*output;
    int t;
    input= fopen("A-small-attempt0.in","r");
    output=fopen("A-small-attempt0.out","w");
    fscanf(input,"%d",&t);
    int test=0;
    for(test=1;test<=t;test++)
    {
        int ans1;
        int arr1[4][4];
        fscanf(input,"%d",&ans1);
        int i,j;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(input,"%d",&arr1[i][j]);
            }
        }
        int ans2;
        int arr2[4][4];
        fscanf(input,"%d",&ans2);
        //int i,j;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(input,"%d",&arr2[i][j]);
            }
        }
        int num=-1;
        int numnum=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr1[ans1-1][i]==arr2[ans2-1][j])
                {
                    numnum++;
                    num=arr1[ans1-1][i];
                }
            }
        }
        if(numnum==1)
        {
            fprintf(output,"Case #%d: %d\n",test,num);
        }
        else if(numnum==0)
        {
            fprintf(output,"Case #%d: Volunteer cheated!\n",test);
        }
        else
        {
            fprintf(output,"Case #%d: Bad magician!\n",test);
        }
    }
    return 0;
}
