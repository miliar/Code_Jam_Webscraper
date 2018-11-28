#include<stdio.h>
#include<stdlib.h>

void printResult(char won,int cases,FILE *pt){
    fprintf(pt,"Case #%d: %c won\n",cases,won);
    printf("Case #%d: %c won\n",cases,won);
}

int main(){
    FILE *pt = fopen("out.txt","a");
    int i,j,k,l,c,t,h;
    char b[6][10],won,current;

    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%s",b[0]);
        scanf("%s",b[1]);
        scanf("%s",b[2]);
        scanf("%s",b[3]);
        //scanf("\n");
        //check first diagonal
        c=1;
        current=b[0][0];
        if(current=='T')
            current=b[1][1];
        for(j=0;j<4;j++){
            if(b[j][j]=='T')
                continue;
            if(b[j][j]!=current){
                c=0;
                break;
            }
        }
        if(c==1){
            if(current!='.'){
                printResult(current,i+1,pt);
            continue;
            }

        }
        //check second diagonal
        c=1;
         current=b[0][3];
        if(current=='T')
            current=b[1][2];
        for(j=3,h=0;j>=0;j--,h++){
            if(b[h][j]=='T')
                continue;
            if(b[h][j]!=current){
                c=0;
                break;
            }
        }

        if(c==1){
                if(current!='.'){
                printResult(current,i+1,pt);
                continue;
                }
                        }

        //check rows
        for(j=0;j<4;j++){
            c=1;
            current=b[j][0];
            if(current=='T')
                current=b[j][1];

            for(k=0;k<4;k++){
                if(b[j][k]=='T')
                continue;
                if(b[j][k]!=current){
                c=0;
                break;
                }
            }
            if(c==1){
                    if(current!='.'){
                    printResult(current,i+1,pt);
                    break;
                    }
                    else c=0;
            }
        }
        if(c==1)
            continue;

        //check columns
        for(j=0;j<4;j++){
            c=1;
             current=b[0][j];
            if(current=='T')
                current=b[1][j];

            for(k=0;k<4;k++){
                if(b[k][j]=='T')
                continue;
                if(b[k][j]!=current){
                c=0;
                break;
                }
            }
            if(c==1){
                    if(current!='.'){
                printResult(current,i+1,pt);
                break;
                    }
                    else c=0;
            }
        }
        if(c==1)
            continue;

        //draw or not yet done
        int draw = 1;
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                if(b[j][k]=='.'){
                    draw = 0;
                    break;
                }
            }
            if(draw == 0)
                break;
        }
        if(draw == 1){
                fprintf(pt,"Case #%d: Draw\n",i+1);
            printf("Case #%d: Draw\n",i+1);
        }
        else{
            fprintf(pt,"Case #%d: Game has not completed\n",i+1);
            printf("Case #%d: Game has not completed\n",i+1);
        }

    }

    fclose(pt);
}
