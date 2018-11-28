#include<stdio.h>
#include<iostream>
using namespace std;
int sign[16];
int main()
{
    int round=0,r=1,row1,row2,row=4,card1[5][5],card2[5][5],res=0;
    FILE *fp, *wfp;
    fp=fopen("A-small-attempt1.in","r+");
    wfp=fopen("A-small-attempt0.out","w+");
    fscanf(fp,"%d",&round);
    while(r<=round){
        res=0;
        for(int i=0;i<17;i++)
            sign[i]=0;
        fscanf(fp,"%d",&row1);
        for(int i=0;i<row;i++)
            for(int j=0;j<row;j++)
                fscanf(fp,"%d",&card1[i][j]);
        fscanf(fp,"%d",&row2);
        for(int i=0;i<row;i++)
            for(int j=0;j<row;j++)
                fscanf(fp,"%d",&card2[i][j]);
        for(int i=0;i<row;i++)
            sign[card1[row1-1][i]]++;
        for(int i=0;i<row;i++){
            if(sign[card2[row2-1][i]]!=0&&res==0)
                res=card2[row2-1][i];
            else if (sign[card2[row2-1][i]]!=0&&res!=0){
                res=-1;
                break;
            }
            else continue;
        }
        fprintf(wfp,"Case #%d: ",r);
        if(res==-1)
            fprintf(wfp,"Bad magician!\n");
        else if(res==0)
            fprintf(wfp,"Volunteer cheated!\n");
        else fprintf(wfp,"%d\n",res);
        r++;
    }



    fclose(fp);
    fclose(wfp);
    return 0;
}
