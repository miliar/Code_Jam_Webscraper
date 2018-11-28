#include <stdio.h>
#include <memory.h>
char one[4][4],two[4][4];

bool X_win_one()
{

    bool one_row_full = false;
    for(int i=0;i<4;i++){

        bool this_row_full = true;
        for(int j=0;j<4;j++){
            if(one[i][j] != 'X'){
                this_row_full = false;
                break;
            }
        }

        if(this_row_full){
            one_row_full = true;
            break;
        }

    }

    bool one_col_full = false;
    for(int i=0;i<4;i++){

        bool this_col_full = true;
        for(int j=0;j<4;j++){
            if(one[j][i] != 'X'){
                this_col_full = false;
                break;
            }
        }

        if(this_col_full){
            one_col_full = true;
            break;
        }

    }

    bool one_dia_full = false;

    bool dia1 = true;
    for(int i=0;i<4;i++){
        if(one[i][i] != 'X'){
            dia1 = false;
            break;
        }
    }

    bool dia2 = true;
    for(int i=0;i<4;i++){
        if(one[i][3-i] != 'X'){
            dia2 = false;
            break;
        }
    }

    one_dia_full = dia1 || dia2;

    return one_col_full || one_row_full || one_dia_full;
}

bool X_win_two()
{

    bool one_row_full = false;
    for(int i=0;i<4;i++){

        bool this_row_full = true;
        for(int j=0;j<4;j++){
            if(two[i][j] != 'X'){
                this_row_full = false;
                break;
            }
        }

        if(this_row_full){
            one_row_full = true;
            break;
        }

    }

    bool one_col_full = false;
    for(int i=0;i<4;i++){

        bool this_col_full = true;
        for(int j=0;j<4;j++){
            if(two[j][i] != 'X'){
                this_col_full = false;
                break;
            }
        }

        if(this_col_full){
            one_col_full = true;
            break;
        }

    }

    bool one_dia_full = false;

    bool dia1 = true;
    for(int i=0;i<4;i++){
        if(two[i][i] != 'X'){
            dia1 = false;
            break;
        }
    }

    bool dia2 = true;
    for(int i=0;i<4;i++){
        if(two[i][3-i] != 'X'){
            dia2 = false;
            break;
        }
    }

    one_dia_full = dia1 || dia2;


    return one_col_full || one_row_full || one_dia_full;
}

bool O_win_one()
{
    bool one_row_full = false;
    for(int i=0;i<4;i++){

        bool this_row_full = true;
        for(int j=0;j<4;j++){
            if(one[i][j] != 'O'){
                this_row_full = false;
                break;
            }
        }

        if(this_row_full){
            one_row_full = true;
            break;
        }

    }

    bool one_col_full = false;
    for(int i=0;i<4;i++){

        bool this_col_full = true;
        for(int j=0;j<4;j++){
            if(one[j][i] != 'O'){
                this_col_full = false;
                break;
            }
        }
        //printf("%d %d\n",i,this_col_full);
        if(this_col_full){
            one_col_full = true;
            break;
        }

    }
    //printf("O:col == %d\n",one_col_full);

    bool one_dia_full = false;

    bool dia1 = true;
    for(int i=0;i<4;i++){
        if(one[i][i] != 'O'){
            dia1 = false;
            break;
        }
    }

    bool dia2 = true;
    for(int i=0;i<4;i++){
        if(one[i][3-i] != 'O'){
            dia2 = false;
            break;
        }
    }

    one_dia_full = dia1 || dia2;

    return one_col_full || one_row_full || one_dia_full;
}


bool O_win_two()
{
    bool one_row_full = false;
    for(int i=0;i<4;i++){

        bool this_row_full = true;
        for(int j=0;j<4;j++){
            if(two[i][j] != 'O'){
                this_row_full = false;
                break;
            }
        }

        if(this_row_full){
            one_row_full = true;
            break;
        }

    }

    bool one_col_full = false;
    for(int i=0;i<4;i++){

        bool this_col_full = true;
        for(int j=0;j<4;j++){
            if(two[j][i] != 'O'){
                this_col_full = false;
                break;
            }
        }

        if(this_col_full){
            one_col_full = true;
            break;
        }

    }

    bool one_dia_full = false;

    bool dia1 = true;
    for(int i=0;i<4;i++){
        if(two[i][i] != 'O'){
            dia1 = false;
            break;
        }
    }

    bool dia2 = true;
    for(int i=0;i<4;i++){
        if(two[i][3-i] != 'O'){
            dia2 = false;
            break;
        }
    }

    one_dia_full = dia1 || dia2;

    return one_col_full || one_row_full || one_dia_full;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("w.out","w",stdout);
    int n;
    scanf("%d",&n);
    int tr,tc;

    memset(one,0,sizeof(one));
    memset(two,0,sizeof(two));

    for(int cs=0;cs<n;cs++){
        tr = tc = -1;
        bool is_t_exist = false;
        int n_dot = 0;
        bool is_full = true;
        for(int i=0;i<4;i++){
            char t[6];
            scanf("%s",t);
            for(int j=0;j<strlen(t);j++){
                one[i][j] = t[j];
                two[i][j] = t[j];
                if(t[j]== 'T'){
                    tr = i;
                    tc = j;
                    is_t_exist = true;
                }
                else if(t[j] == '.'){
                    n_dot++;
                }
                //printf("%c",t[j]);
            }
            //printf("\n");
        }
        if(n_dot){
            is_full = false;
        }
        //printf("%d %d\n",tr,tc);

        if(is_t_exist){
            one[tr][tc] = 'O';
            two[tr][tc] = 'X';
        }

        printf("Case #%d: ",cs+1);

        if(X_win_one() || X_win_two()){
            //printf("%d %d\n",X_win_one(),X_win_two());

            printf("X won\n");
        }else if(O_win_one() || O_win_two()){
            //printf("%d %d\n",O_win_one(),O_win_two());
            printf("O won\n");
        }
        else{
            if(is_full){
                //draw
                printf("Draw\n");
            }
            else{
                //not complete
                printf("Game has not completed\n");
            }
        }
    }
    return 0;
}
