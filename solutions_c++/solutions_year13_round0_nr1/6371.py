#include<stdio.h>
#include<vector>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
        int t,num=1;
        scanf("%d",&t);
        while(t--)
        {
            char arr[4][5];
            int i,j,dot=0,t_row,t_col,x=0,o=0,sum=0;
            for(i=0;i<4;i++)
                scanf("%s",arr[i]);
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(arr[i][j]=='.')
                        dot++;
                }
            }
            for(i=0;i<4;i++)
            {
                    sum=arr[i][0]+arr[i][1]+arr[i][2]+arr[i][3];
                    if(sum==321||sum==316)
                        o++;
                    else if(sum==348||sum==352)
                        x++;
            }
            for(j=0;j<4;j++)
            {
                    sum=arr[0][j]+arr[1][j]+arr[2][j]+arr[3][j];
                    if(sum==321||sum==316)
                        o++;
                    else if(sum==348||sum==352)
                        x++;
            }
            sum=arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3];
            if(sum==348||sum==352)
                x++;
            if(sum==321||sum==316)
                o++;
            sum=arr[3][0]+arr[2][1]+arr[1][2]+arr[0][3];
             if(sum==348||sum==352)
                x++;
            if(sum==321||sum==316)
                o++;
            printf("Case #%d: ",num++);
            if(dot)
            {
                if(x>o)
                    printf("X won\n");
                else if(o>x)
                    printf("O won\n");
                else
                    printf("Game has not completed\n");
            }
            else
            {
                if(x>o)
                    printf("X won\n");
                else if(o>x)
                    printf("O won\n");
                else
                    printf("Draw\n");
            }
        }
    return 0;
}
