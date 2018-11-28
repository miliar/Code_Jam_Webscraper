#include<stdio.h>
#include<iostream>

using namespace std;

FILE * pFile;

int compute()
{
    int ans1,ans2;
    int cards1[4][4],cards2[4][4];

    int i,j;
    fscanf(pFile,"%d",&ans1);
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            fscanf(pFile,"%d",&cards1[i][j]);
    }

    fscanf(pFile,"%d",&ans2);
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            fscanf(pFile,"%d",&cards2[i][j]);
    }

    int count=0;
    int ans;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(cards1[ans1-1][i]==cards2[ans2-1][j])
            {
                count++;
                ans=cards1[ans1-1][i];
            }
            if(count>1)
                return -1;
        }
    }
    if(count==0)
        return 0;
    else
        return ans;
}


int main()
{
    int i,t;
    pFile = fopen ("myfile.txt","r+");
    fscanf(pFile,"%d",&t);
    for(i=0;i<t;i++)
    {
        int ans=compute();
        printf("Case #%d: ",i+1);
        switch(ans)
        {
            case 0 : printf("Volunteer cheated!\n");
                     break;
            case -1 : printf("Bad magician!\n");
                      break;
            default : printf("%d\n",ans);
                    break;
        }
    }

    return 0;
}
