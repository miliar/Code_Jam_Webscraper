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
        // �e�s dr �ɂ��āA for ddc max(h[dr][ddc]) �܂łȂ犠�����B
        // ��������Ⴂ�I�[�_�[�͗�����̊�����Ɋ��҂��邵���Ȃ��B
        // ������������� maxCH[col] �܂ł������Ȃ��̂ŁA�����Ŗ�������������A�E�g�B
        possible = true;
        for(int row = 0;row < N && possible;++row){
            for(int col = 0;col < M && possible;++col){
                if( m[row][col] < maxRH[row] ){
                    // ������΂�
                    // col �ō��Ȃ�������A�E�g
                    if( m[row][col] < maxCH[col] ){
                        // �͂����߁[
                        possible = false;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %s\n",r+1,possible?"YES":"NO");
    }

}