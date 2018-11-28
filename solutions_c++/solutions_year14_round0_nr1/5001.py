#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("small.out","wt",stdout);
    
    int t;
    scanf("%d",&t);
    for(int ctr=1;ctr <=t;ctr++)
    {
        int num1;
        scanf("%d",&num1);
        int array1[4];
       for(int i=0;i<4;i++)
       {
            for(int j=0;j<4;j++)
            {
                if(i+1 == num1)
                    scanf("%d",&array1[j]);
                else {
                    int temp;
                    scanf("%d",&temp);
                }
            }
       }
        
        int num2;
        scanf("%d",&num2);
        int array2[4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(i+1 == num2)
                    scanf("%d",&array2[j]);
                else {
                    int temp;
                    scanf("%d",&temp);
                }
            }
        }
        int ans =0;
        int value;
    
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(array1[i] == array2[j])
                {
                    ans++;
                    value= array1[i];
                }
            }
        }
        
        if(ans== 1)
            printf("Case #%d: %d\n",ctr,value);
        else if(ans > 1)
            printf("Case #%d: Bad magician!\n",ctr);
        else if(ans == 0)
            printf("Case #%d: Volunteer cheated!\n",ctr);
    }
    return 0;
}