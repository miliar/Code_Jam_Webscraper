#include<stdio.h>



int judge(int b[4][4],int b2[4][4], int r1, int r2 )
{
    int temp[17]={0};
    for(int i=0; i<4; i++) 
    {
        temp[b[r1][i]]++;
        temp[b2[r2][i]]++;
    }
    int sum=0;
    for(int i=1; i<17; i++)
        if(temp[i]==2)
            sum++;

    if(sum==0)
        return sum;

    if(sum>1)
        return -1;

    for(int i=1; i< 17; i++)
        if(temp[i] == 2)
            return i;    
}





int main(int argc, char** argv)
{
    FILE *file = fopen("tic.in","r"); 
    FILE *out = fopen("tic.out","w");
    int n=0;
    fscanf(file,"%d",&n);

    for(int i=0; i<n; ++i)
    {
        int baord[4][4];
        int baord1[4][4];
        int row1,row2;
        fscanf(file,"%d",&row1);

        for(int j=0; j<4; ++j)
            for(int k=0; k<4; ++k)
            {
                fscanf(file,"%d", &baord[j][k]);
            }
        
        fscanf(file,"%d",&row2);
        for(int j=0; j<4; ++j)
            for(int k=0; k<4; ++k)
            {
                fscanf(file,"%d", &baord1[j][k]);
            }
        int sum = judge(baord,baord1,row1-1,row2-1);
        
        fprintf(out,"Case #%d: ",i+1);
        if(sum > 0)
            fprintf(out,"%d\n",sum);
        if(sum < 0)
            fprintf(out,"Bad magician!\n");
        if(sum == 0)
            fprintf(out,"Volunteer cheated!\n");
            

    }

    fclose(file);
    fclose(out);
    return 0;
}
