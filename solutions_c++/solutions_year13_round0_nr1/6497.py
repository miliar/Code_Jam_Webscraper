#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
char str[1001][5],result[11][6],possible[11][6];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    int i,j,n,test,test1,k;
    strcpy(possible[0],"XXXX");
    strcpy(possible[1],"OOOO");
    strcpy(possible[2],"XXXT");
    strcpy(possible[3],"OOOT");
    strcpy(possible[4],"TXXX");
    strcpy(possible[5],"TOOO");
    strcpy(possible[6],"XTXX");
    strcpy(possible[7],"OTOO");
    strcpy(possible[8],"XXTX");
    strcpy(possible[9],"OOTO");
    while(scanf("%d",&n)==1){
        for(i=1;i<=n;i++){
            scanf("%s",&str[0]);
            scanf("%s",&str[1]);
            scanf("%s",&str[2]);
            scanf("%s",&str[3]);
            strcpy(result[0],str[0]);
            strcpy(result[1],str[1]);
            strcpy(result[2],str[2]);
            strcpy(result[3],str[3]);

            result[4][0]=str[0][0];
            result[4][1]=str[1][0];
            result[4][2]=str[2][0];
            result[4][3]=str[3][0];
            result[4][4] = NULL;

            result[5][0]=str[0][1];
            result[5][1]=str[1][1];
            result[5][2]=str[2][1];
            result[5][3]=str[3][1];
            result[5][4] = NULL;
            result[6][0]=str[0][2];
            result[6][1]=str[1][2];
            result[6][2]=str[2][2];
            result[6][3]=str[3][2];
            result[6][4] = NULL;
            result[7][0]=str[0][3];
            result[7][1]=str[1][3];
            result[7][2]=str[2][3];
            result[7][3]=str[3][3];
            result[7][4] = NULL;
            result[8][0]=str[0][0];
            result[8][1]=str[1][1];
            result[8][2]=str[2][2];
            result[8][3]=str[3][3];
            result[8][4] = NULL;
            result[9][0]=str[0][3];
            result[9][1]=str[1][2];
            result[9][2]=str[2][1];
            result[9][3]=str[3][0];
            result[9][4] = NULL;
            test = 0;
            for(j=0;j<10&&test!=1;j++){
                //printf("[%s]\n",result[j]);
                for(k=0;k<10&&test!=1;k++){
                    if(strcmp(possible[j],result[k])==0){
                        if(j%2==0){
                            printf("Case #%d: X won\n",i);
                            test = 1;
                            break;
                        }else{
                            printf("Case #%d: O won\n",i);
                            test =1;
                            break;
                        }

                    }
                }
            }
            test1 = 0;
            if(test == 0){
                for(j=0;j<4&&test1!=1;j++){
                    for(k=0;k<4&&test1!=1;k++){
                        if(str[j][k]=='.'){
                            printf("Case #%d: Game has not completed\n",i);
                            test1 = 1;
                            break;
                        }
                    }
                }
            }
            if(test1 == 0 && test == 0){
                printf("Case #%d: Draw\n",i);
            }
        }
    }
    fclose(stdin);
    fclose(stdout);
return 0;
}
