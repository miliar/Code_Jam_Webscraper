#include <iostream>
#include<cstdio>

using namespace std;

int main()
{
    int T,first_arrang[4][4],second_arrang[4][4];
    int first_choice,second_choice;
    int i,j;
    int cell;
    int case_no=1;
    int flag,count;
    scanf("%d",&T);
    while(T)
    {
        scanf("%d",&first_choice);
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            scanf("%d",&first_arrang[i][j]);
        scanf("%d",&second_choice);
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            scanf("%d",&second_arrang[i][j]);
        cell=-1;flag=0;count=0;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {
            if(first_arrang[first_choice-1][i]==second_arrang[second_choice-1][j])
            {
                flag=1;count=count+1;cell=i;
            }
        }
        if(flag==1 && count==1)
            printf("Case #%d: %d\n",case_no,first_arrang[first_choice-1][cell]);
        else if(flag==0 && count==0)
            printf("Case #%d: Volunteer cheated!\n",case_no);
        else //if(flag==0 && count>1)
            printf("Case #%d: Bad magician!\n",case_no);
        case_no+=1;
        T--;
    }
    return 0;
}
