#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t;
int array[4][4];
int hash[17];
int row;


int main()
{
    freopen("A--small-attempt0.in","r",stdin);
    freopen("A--small-attempt0_out.txt","w",stdout);
    
    int i,j;
    scanf("%d",&t);
    
    for(int tt = 1; tt <= t; tt++)
    {
        memset(hash, 0, sizeof(hash));
        scanf("%d",&row);
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                scanf("%d",&array[i][j]);
                if(i == row-1)
                {
                    hash[array[i][j]]++;
                }
            }
        }
        
        
        scanf("%d",&row);
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                scanf("%d",&array[i][j]);
                if(i == row-1)
                {
                    hash[array[i][j]]++;
                }
            }
        }
        
        int count=0;
        int num;
        for(i=1; i <=16; i++)
        {
            if(hash[i]==2)
            {
                count++;
                num = i;
            }
        }
        
        printf("Case #%d: ", tt);
        if(count == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(count == 1)
        {
            printf("%d\n",num);
        }
        else
        {
            printf("Bad magician!\n");
        }
        
        
    }
    //system("pause");
    return 0;
}
