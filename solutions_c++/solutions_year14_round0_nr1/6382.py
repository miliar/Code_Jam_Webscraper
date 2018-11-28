#include<bits/stdc++.h>

using namespace std;

int main()
{
    FILE *fp,*fo;
    fp=fopen("input1.txt","r");
    fo=fopen("output1.txt","w");
    int t,x;
    fscanf(fp,"%d",&t);
    for(x=1;x<=t;x++){
        int a,b,org[4][4],shuff[4][4],i,j,s[20]={0},f[20]={0},count=0;
        fscanf(fp,"%d",&a);

        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {
            fscanf(fp,"%d",&org[i][j]);
            if(i==a-1)
            s[org[i][j]]=1;

        }

        fscanf(fp,"%d",&b);


        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {
            fscanf(fp,"%d",&shuff[i][j]);
            if(i==b-1)
            f[shuff[i][j]]=1;

        }

        for(i=1;i<=16;i++)
        {
           if(s[i]&&f[i])
            count++;
        }

        if(count==0)
        fprintf(fo,"Case #%d: Volunteer cheated!\n",x);

        else if(count>1)
        fprintf(fo,"Case #%d: Bad magician!\n",x);

        else if(count==1)
        {
            for(i=1;i<=16;i++)
            if(s[i]&&f[i])
            break;

            fprintf(fo,"Case #%d: %d\n",x,i);

        }




    }

    fclose(fp);
    fclose(fo);
    return 0;
}
