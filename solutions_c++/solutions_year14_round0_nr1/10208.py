#include <cstdlib>
#include<stdio.h>
using namespace std;
int first[4][4];
int second[4][4];

int FindResult(int first_sel,int second_sel)
{
    int ret = 0,no_of_matches = 0;
    for(int i = 0;i<4;i++)
        for(int j = 0;j<4;j++)
    {
        if(first[first_sel-1][i] == second[second_sel-1][j])
        {
            ret =  first[first_sel-1][i];
            no_of_matches++;
        }
    }
    if(no_of_matches > 1)
        ret = -1;
    return ret;
}
int main(int argc, char** argv) {
    int no_of_test_cases;
    int first_sel;
    int sec_sel;
    freopen("Magic.txt" ,"r+",stdin);
    freopen("Magic_out.txt" ,"w+",stdout);
    scanf("%d\n",&no_of_test_cases);
    for(int i = 0;i<no_of_test_cases;i++)
    {
        scanf("%d",&first_sel);
        for(int j = 0;j<4;j++)
          for(int k = 0;k<4;k++)
            scanf("%d",&first[j][k]);
        scanf("%d",&sec_sel);
        for(int j = 0;j<4;j++)
          for(int k = 0;k<4;k++)
            scanf("%d",&second[j][k]);
        
        int val = FindResult(first_sel,sec_sel);
        switch(val)
        {
            case -1: printf("Case #%d: Bad magician!\n",i+1);
                     break;
            case 0:  printf("Case #%d: Volunteer cheated!\n",i+1);
                     break;
            default: printf("Case #%d: %d\n",i+1,val);
                     break;
        }
        
    }        
}

