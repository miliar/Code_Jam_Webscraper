#include<stdio.h>
int main()
{
    int t,full,i,j,X_win,O_win,count,K=1,sum;
    char s[5][5];
    scanf("%d",&t);
    while(t--)
    {
            printf("Case #%d: ",K);
            K++;
            full=1,X_win=0,O_win=0;
            for(i=0;i<4;i++)
                    scanf("%s",s[i]);
            count=0;
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(s[i][j]=='.')
                        count++;
                }
            }
            if(count>0)
                full=0;
            //horizontally//
            for(i=0;i<4;i++)
            {
                sum=0;
                for(j=0;j<4;j++)
                {
                      sum+=s[i][j];
                }
                if(sum==348||sum==352){
                    X_win=1;
                    goto end;
                }
                if(sum==321||sum==316)
                {
                    O_win=1;
                    goto end;
                }
            }
            //vertically//
            for(i=0;i<4;i++)
            {
		sum=0;
                for(j=0;j<4;j++)
                {
                    sum+=s[j][i];
                }
                if(sum==348||sum==352){
                    X_win=1;
                    goto end;
                }
                if(sum==321||sum==316)
                {
                    O_win=1;
                    goto end;
                }
            }
            sum=0;
            //diagonally//
            sum=s[0][0]+s[1][1]+s[2][2]+s[3][3];
            if(sum==348||sum==352)
                X_win=1;
            if(sum==321||sum==316)
                O_win=1;
            sum=0;
            sum=s[3][0]+s[2][1]+s[1][2]+s[0][3];
             if(sum==348||sum==352)
                X_win=1;
            if(sum==321||sum==316)
                O_win=1;
            end:
            if(full)
            {
                if(X_win)
                    printf("X won\n");
                else if(O_win)
                    printf("O won\n");
                else
                    printf("Draw\n");
            }
            else
            {
                if(X_win)
                    printf("X won\n");
                else if(O_win)
                    printf("O won\n");
                else
                    printf("Game has not completed\n");
            }
    }
    return 0;
}
