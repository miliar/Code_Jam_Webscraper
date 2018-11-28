#include<stdio.h>
#include<string.h>
int main(){
    char ch[4][4];
    int glob=0;
    int t,i,j,k,flag;
    int xcnt,ocnt,tcnt;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        glob=0;
        for(j=0;j<4;j++)
        scanf("%s",ch[j]);

         for(j=0;j<4;j++){
            flag=0;
            xcnt=0;ocnt=0;tcnt=0;
            for(k=0;k<4;k++){
                if(ch[j][k]=='.'){
                    glob++;
                    break;
                }
                else if(ch[j][k]=='T')
                {
                    tcnt++;
                    if(tcnt>1)
                    break;
                }
                else if(ch[j][k]=='O')
                ocnt++;
                else if(ch[j][k]=='X')
                xcnt++;
            }
            if(xcnt==4 ||(xcnt==3 && tcnt==1)){
                printf("Case #%d: X won\n",i);
                flag=1;
                break;
            }
            else if(ocnt==4 ||(ocnt==3 && tcnt==1)){
                printf("Case #%d: O won\n",i);
                flag=1;
                break;
            }
        }

        if(flag==1)
        continue;

        for(k=0;k<4;k++){
            xcnt=0;ocnt=0;tcnt=0;flag=0;
            for(j=0;j<4;j++){
                if(ch[j][k]=='.'){
                    glob++;
                    break;
                }
                else if(ch[j][k]=='T')
                {
                    tcnt++;
                    if(tcnt>1)
                    break;
                }
                else if(ch[j][k]=='O')
                ocnt++;
                else if(ch[j][k]=='X')
                xcnt++;
            }
            if(xcnt==4 ||(xcnt==3 && tcnt==1)){
                printf("Case #%d: X won\n",i);
                flag=1;
                break;
            }
            else if(ocnt==4 ||(ocnt==3 && tcnt==1)){
                printf("Case #%d: O won\n",i);
                flag=1;
                break;
            }
        }
        if(flag==1)
        continue;

         for(k=0;k<2;k++){
            xcnt=0;ocnt=0;tcnt=0;flag=0;
            for(j=0;j<4;j++){
                if(ch[j][j]=='.'){
                    glob++;
                    break;
                }
                else if(ch[j][j]=='T')
                {
                    tcnt++;
                    if(tcnt>1)
                    break;
                }
                else if(ch[j][j]=='O')
                ocnt++;
                else if(ch[j][j]=='X')
                xcnt++;
            }
            if(xcnt==4 ||(xcnt==3 && tcnt==1)){
                printf("Case #%d: X won\n",i);
                flag=1;
                break;
            }
            else if(ocnt==4 ||(ocnt==3 && tcnt==1)){
                printf("Case #%d: O won\n",i);
                flag=1;
                break;
            }
        }
        if(flag==1)
        continue;

        if(glob==0)
        printf("Case #%d: Draw\n",i);
        else
        printf("Case #%d: Game has not completed\n",i);
    }
    return 0;
}
