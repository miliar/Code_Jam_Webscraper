#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int m[1000][1000];
int maxRH[1000];
int maxCH[1000];

int main(void){

    int T;
    scanf("%d",&T);

    for(int r = 0;r < T;++r){
        bool possible = false;
        int N,M;
        scanf("%d %d",&N,&M);
        for(int row = 0;row < N;++row){
            maxRH[row] = 0;
            for(int col = 0;col < M;++col){
                scanf("%d",&m[row][col]);
                maxRH[row] = maxRH[row] < m[row][col] ? m[row][col] : maxRH[row];
            }
        }
        for(int col = 0;col < M;++col){
            maxCH[col] = 0;
            for(int row = 0;row < N;++row){
                maxCH[col] = maxCH[col] < m[row][col] ? m[row][col] : maxCH[col];
            }
        }
        // 各行 dr について、 for ddc max(h[dr][ddc]) までなら刈り取れる。
        // それよりも低いオーダーは列方向の刈り取りに期待するしかない。
        // しかし列方向も maxCH[col] までしか削れないので、ここで矛盾がおきたらアウト。
        possible = true;
        for(int row = 0;row < N && possible;++row){
            for(int col = 0;col < M && possible;++col){
                if( m[row][col] < maxRH[row] ){
                    // ここやばい
                    // col で削れなかったらアウト
                    if( m[row][col] < maxCH[col] ){
                        // はいだめー
                        possible = false;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %s\n",r+1,possible?"YES":"NO");
    }

}