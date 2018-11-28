// Coded by shubham1402
// DATE :  4/12          TIME :


/**************************************************************
*	Problem code: Magic Trick
*	REFERENCES (if any):
*
*
**************************************************************/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    FILE *fp = fopen("input1.txt","r");
    FILE *op = fopen("out1.txt","w");
    int t;
    fscanf(fp,"%d",&t);
    int k = 1;
    while(t--)
    {
        int r1;
        fscanf(fp,"%d",&r1);
        int arr[4][4];
        int count1[17],count2[17];
        for(int i=0;i<17;i++)
        {
            count1[i] = count2[i] = 0;
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                fscanf(fp,"%d",&arr[i][j]);
                if(i == r1-1)
                {
                    count1[arr[i][j]]++;
                }
            }
        }
        int r2;
        fscanf(fp,"%d",&r2);
        int arr2[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                fscanf(fp,"%d",&arr2[i][j]);
                if(i == r2-1)
                {
                    count2[arr2[i][j]]++;
                }
            }
        }
        int cnt = 0;
        int ind = 0;
        for(int i=0;i<17;i++)
        {
            if(count1[i] == count2[i] && count1[i] == 1)
            {
                cnt++;
                ind = i;
            }
        }
        fprintf(op,"Case #%d: ",k++);
        if(cnt == 0)
        {
            fprintf(op,"Volunteer cheated!\n");
        }
        else if(cnt > 1)
        {
            fprintf(op,"Bad magician!\n");
        }
        else
        {
            fprintf(op,"%d\n",ind);
        }
    }

	return 0;
}
