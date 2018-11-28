#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

#define MAXN 10
int arrange1[MAXN][MAXN];
int arrange2[MAXN][MAXN];

int main(void)
{
    int T, Case, i, j;  
    int ans1, ans2;
    int SameNum, card;
    FILE *fp1,*fp2;
    if((fp1=fopen("A-small-attempt0.in","r"))==NULL)exit(0);
    if((fp2=fopen("A-small-attempt0.out","w"))==NULL)exit(0);
    
    Case = 1;
    fscanf(fp1,"%d",&T);
    while(Case <= T)
    {
        fscanf(fp1,"%d", &ans1);
        for(i = 1; i <= 4; i++)
        {
            for(j = 1; j <= 4; j++)
            {
                fscanf(fp1,"%d", &arrange1[i][j]);
            }
        }
        fscanf(fp1,"%d", &ans2);
        for(i = 1; i <= 4; i++)
        {
            for(j = 1; j <= 4; j++)
            {
                fscanf(fp1,"%d", &arrange2[i][j]);
            }
        }
        
        SameNum = 0;
        card = -1;
        for(i = 1; i <=4; i++)
        {
            for(j = 1; j <= 4; j++)
            {
                if (arrange1[ans1][i] == arrange2[ans2][j])
                {
                    SameNum++;
                    card = arrange1[ans1][i];
                }
            }
        }
        
        if (SameNum == 1)
        {
            fprintf(fp2,"Case #%d: %d\n", Case, card);
        }
        else if (SameNum > 1)
        {
            fprintf(fp2,"Case #%d: Bad magician!\n", Case);
        }
        else
        {
            fprintf(fp2,"Case #%d: Volunteer cheated!\n", Case);
        }
        
        Case++;
    } 
    return 0;
}
