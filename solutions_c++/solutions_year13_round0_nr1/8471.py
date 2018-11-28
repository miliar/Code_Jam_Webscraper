#include<stdio.h>
int main(){
    int T;
    int li,ci;
    int board[4][4];
    int mode;
    char tmp_input;
    int timerX,timerO,timerT;
    bool finished=true,ans=false;
    char header[] = "Case #";
    FILE* pFile_in = fopen("A-small-attempt6.in","r");
    FILE* pFile_out = fopen("t_out.txt","w");
    fscanf(pFile_in,"%d",&T);
    int counter = T;
    while(T>0){
        T--;
        ans=false;
        finished=true;

        for(li=0;li<4;li++){
            for(ci=0;ci<4;ci++){
                    if(ci==0)
                        fscanf(pFile_in,"\n%c",&tmp_input);
                    else
                        fscanf(pFile_in,"%c",&tmp_input);
                    switch (tmp_input){
                        case 'X':board[li][ci]=1;break;
                        case 'O':board[li][ci]=0;break;
                        case 'T':board[li][ci]=-1;break;
                        case '.':board[li][ci]=-2;break;
                    }
            }
        }

        for(li=0;li<4;li++){
            timerX=0;
            timerO=0;
            timerT=0;
            for(ci=0;ci<4;ci++){
                if(board[li][ci]==-2){
                    finished=false;
                    break;
                }
                if(board[li][ci]==1){
                    timerX++;
                }
                else{
                    if(board[li][ci]==0)
                        timerO++;
                    else
                        timerT++;
                }
            }
            if(timerX>3||(timerX==3&&timerT==1)){
                ans=true;
                fprintf(pFile_out,"%s%d: X won\n",header,counter-T);
                break;
            }
            if(timerO>3||(timerO==3&&timerT==1)){
                ans=true;
                fprintf(pFile_out,"%s%d: O won\n",header,counter-T);
                break;
            }
        }
        if(ans==true)
            continue;


        // Deal the column
        for(ci=0;ci<4;ci++){
            timerX=0;
            timerO=0;
            timerT=0;
            for(li=0;li<4;li++){
                if(board[li][ci]==-2){
                    finished=false;
                    break;
                }

                if(board[li][ci]==1){
                    timerX++;
                }
                else{
                    if(board[li][ci]==0)
                        timerO++;
                    else
                        timerT++;
                }
            }
            if(timerX>3||(timerX==3&&timerT==1)){
                ans=true;
                fprintf(pFile_out,"%s%d: X won\n",header,counter-T);
                break;
            }
            if(timerO>3||(timerO==3&&timerO==1)){
                ans=true;
                fprintf(pFile_out,"%s%d: O won\n",header,counter-T);
                break;
            }
        }
        if(ans==true)
            continue;

        timerX=0;
        timerO=0;
        timerT=0;
        for(li=0;li<4;li++){
            if(board[li][li]==-2){
                finished=false;
                break;
            }
            if(board[li][li]==1)
                timerX++;
            else{
                if(board[li][li]==0)
                    timerO++;
                else
                    timerT++;
            }
        }
        if(timerX>3||(timerX==3&&timerT==1)){
            fprintf(pFile_out,"%s%d: X won\n",header,counter-T);
            continue;
        }
        else{
            if(timerO>3||(timerO==3&&timerO==1)){
                fprintf(pFile_out,"%s%d: O won\n",header,counter-T);
                continue;
            }
        }

        timerX=0;
        timerO=0;
        timerT=0;
        for(li=0;li<4;li++){
            if(board[li][3-li]==-2){
                finished=false;
                break;
            }

            if(board[li][3-li]==1)
                timerX++;
            else{
                if(board[li][3-li]==0)
                    timerO++;
                else
                    timerT++;
            }
        }
        if(timerX>3||(timerX==3&&timerT==1)){
            fprintf(pFile_out,"%s%d: X won\n",header,counter-T);
            continue;
        }
        else{
            if(timerO>=3||(timerO==3&&timerT==1)){
                fprintf(pFile_out,"%s%d: O won\n",header,counter-T);
                continue;
            }
        }
        if(finished==true)
            fprintf(pFile_out,"%s%d: Draw\n",header,counter-T);
        else
            fprintf(pFile_out,"%s%d: Game has not completed\n",header,counter-T);
        int c;
        fscanf(pFile_in,"%c",&c);
    }
    return 0;
}
