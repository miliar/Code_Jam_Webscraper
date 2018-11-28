#include<stdio.h>

int main(){
    int t, n;
    char str[2][101];
    scanf("%d",&t);
    for(int i =1;i<=t;i++){
        scanf("%d",&n);
        for(int j = 0; j<n;j++){
            scanf("%s",str[j]);
        }

        int m=0,n=0,step=0,got=0;

        while(str[0][m]!='\0'&&str[1][n]!='\0'){
            if(str[0][m]==str[1][n]){
                m++;
                n++;
                got=1;
            }
            else{
                if(m>0&&n>0){
                    if(str[0][m] == str[0][m-1]){
                        m++;
                        step++;
                    }
                    else if(str[1][n] == str[1][n-1]){
                        n++;
                        step++;
                    }
                    else{
                        step = -1;
                        break;
                    }
                }
                else{
                    step = -1;
                    break;
                }
            }
        }
        if(got){
            while(str[0][m]!='\0'){
                if(str[0][m-1]==str[0][m]){
                    m++;
                    step++;
                }
                else{
                    step = -1;
                    break;
                }
            }
            while(str[1][n]!='\0'){
                if(str[1][n-1]==str[1][n]){
                    n++;
                    step++;
                }
                else{
                    step = -1;
                    break;
                }
            }
        }
        if(step==-1)
            printf("Case #%d: Fegla Won\n",i);
        else printf("Case #%d: %d\n",i,step);
    }
}
