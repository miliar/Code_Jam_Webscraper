#include<stdio.h>

char a[5][5];
int full,t;



int win(){
    int i,j,cx,co;
    for ( i = 1; i <= 4; i++ ){
        cx = 0;
        co = 0;
        for ( j = 1; j <=4; j++ ){
            if ( a[i][j] == 'T' ) {
                cx++;
                co++;
            }
            if ( a[i][j] =='O' ) co++;
            if ( a[i][j] =='X' ) cx++;
        }
        // printf("x  %d  O  %d\n",cx,co);
        if ( cx == 4 ) return 1;
        if ( co == 4 ) return 2;
    }
    for ( j = 1; j <= 4; j++ ){
        cx = 0;
        co = 0;
        for ( i = 1; i <=4; i++ ){
            if ( a[i][j] == 'T' ) {
                cx++;
                co++;
            }
            if ( a[i][j] =='O' ) co++;
            if ( a[i][j] =='X' ) cx++;
        }
        if ( cx == 4 ) return 1;
        if ( co == 4 ) return 2;
    }
    cx = 0;
    co = 0;
    for ( i = 1; i <= 4; i++ ){
        if ( a[i][i] == 'T' ) {
                cx++;
                co++;
            }
        if ( a[i][i] =='O' ) co++;
        if ( a[i][i] =='X' ) cx++;
    }
    if ( cx == 4 ) return 1;
    if ( co == 4 ) return 2;
    cx = 0;
    co = 0;
    for ( i = 1; i <= 4; i++ ){
        if ( a[5-i][i] == 'T' ) {
                cx++;
                co++;
            }
        if ( a[5-i][i] =='O' ) co++;
        if ( a[5-i][i] =='X' ) cx++;
    }
    if ( cx == 4 ) return 1;
    if ( co == 4 ) return 2;
    if ( full == 16 ) return 3;
    return 0;
}

void solve( ){
    int i,x,y;
    FILE* fin = fopen("E:\\g3.in","r");
    FILE* fout = fopen("E:\\gout.txt","w");
    fscanf(fin,"%d",&t);
    for ( i = 1; i <= t; i++ ){
        full = 0;
        fgetc(fin);
        for ( x = 1; x <= 4; x++ ){
            for ( y = 1; y <= 4; y++ ){
                fscanf(fin,"%c",&a[x][y]);
                if ( a[x][y] != '.' ) full++;
            }
            fgetc(fin);
        }
        fprintf(fout,"Case #%d: ",i);
        int temp = win();
        if ( temp == 1 ) fprintf(fout,"X won\n");
        if ( temp == 2 ) fprintf(fout,"O won\n");
        if ( temp == 3 ) fprintf(fout,"Draw\n");
        if ( temp == 0 ) fprintf(fout,"Game has not completed\n");
    }
    fclose(fin);
    fclose(fout);
}

main(){
    solve();
}
