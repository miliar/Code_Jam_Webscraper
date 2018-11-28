#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int N;
int s[3];

char ans[5000];
char tmp_ans[5000];

int lose(char a){
    if(a == 'R')return 'S';
    if(a == 'S')return 'P';
    if(a == 'P')return 'R';
    return '\0';
}

int gen_ans(int N, int flag){
    for(int i=0;i<5000;i++)ans[i] = 0;
    if(flag == 0){
        ans[0] = 'R';
    }
    if(flag == 1){
        ans[0] = 'P';
    }
    if(flag == 2){
        ans[0] = 'S';
    }

    int max = 1;
    for(int i=0;i<N;i++){
        for(int j=0;j<max;j++){
            if(ans[j] == 'R'){
                tmp_ans[2 * j] = 'R';
                tmp_ans[2 * j + 1] = 'S';
            }else if(ans[j] == 'S'){
                tmp_ans[2 * j] = 'P';
                tmp_ans[2 * j + 1] = 'S';
            }else if(ans[j] == 'P'){
                tmp_ans[2 * j] = 'P';
                tmp_ans[2 * j + 1] = 'R';
            }
        }
        max *= 2;
        for(int j=0;j<max;j++){
            ans[j] = tmp_ans[j];
        }
    }


    int wid = 2;
    char tmp[5000];
    while(wid <= max){
        for(int j=0;j<max;j+=wid){
            if(strncmp(ans + j, ans + j + wid / 2, wid / 2) > 0){
                strncpy(tmp              , ans + j          , wid / 2);
                strncpy(ans + j          , ans + j + wid / 2,  wid / 2);
                strncpy(ans + j + wid / 2, tmp              ,  wid / 2);
            }
        }
        wid *= 2;
    }


    return 0;
}



int main(){
    int T;
    scanf("%d",&T);
    for(int ca= 1;ca <=T;ca++){

        scanf("%d %d %d %d", &N, &s[0], &s[1], &s[2]);

        printf("Case #%d: ", ca);
        
        
        int count[3][3];
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++)
                count[i][j] = 0;
        }




        for(int k=0;k<3;k++){
            count[k][k] = 1;
            for(int i=0;i<N;i++){ 
                int tmp[3];
                tmp[0] = tmp[1] = tmp[2] = 0;

                tmp[0] = count[k][0] + count[k][1];
                tmp[1] = count[k][1] + count[k][2];
                tmp[2] = count[k][2] + count[k][0];

                count[k][0] = tmp[0];
                count[k][1] = tmp[1];
                count[k][2] = tmp[2];
            }
        }
        
        int flag = -1;
        for(int i=0;i<3;i++){
            
            if(count[i][0] == s[0] && count[i][1] == s[1] && count[i][2] == s[2]){
                flag = i;
                break;
            }
        }

        if(flag == -1){
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        
        gen_ans(N, flag);
        
        printf("%s\n",ans);

    }
    return 0;
}
