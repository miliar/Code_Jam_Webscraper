#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

typedef long long ll;

char data[ 20000 ];

int main(void){

    int T;
    scanf("%d",&T);

    for(int round = 0;round < T;++round){
        // �X���[�������B
        // �܂����E�����ɃK�K�K�K�b�ƐU���āAX�����킹��B
        // ���ɁA�c�����́A�ړI�n����щz���͈͂ɓ����Ă��܂��Ă���Ȃ�A
        // 2���щz���āA�K�K�K�K�b�Ƃ��B
        // �����ĂȂ��Ȃ�A�ړI�n�����ɔ��ŃK�K�K�K�b�Ƃ��B
        int x = 0;
        int y = 0;
        int gx;
        int gy;
        scanf("%d %d",&gx,&gy);
        int turn = 0;
        // X ����
        while(x != gx){
            data[ turn ] = 'E';
            x += ++turn;
            if( x == gx ) break;
            data[ turn ] = 'W';
            x -= ++turn;
            if( x == gx ) break;
        }
        // Y ����
        // turn + 1 �ŃW�����v���āA
        // ��щz���Ȃ��Ȃ�A����ł����B
        // ��щz����悤�Ȃ�A�t�ɔ�ԁB
        int sig = gy < 0 ? -1 : 1;
        if( y != gy ){
            if( sig > 0 ){
                if( y < y + turn + 1 ){
                    // ��щz�����Ⴄ
                    sig = -sig;
                }
            }else{
                if( y > y - turn - 1 ){
                    sig = -sig;
                }
            }
            while(y != gy){
                if( sig > 0 ){
                    data[ turn ] = 'N';
                }else{
                    data[ turn ] = 'S';
                }
                y += ++turn * sig;
                sig = -sig;
            }
        }
        data[ turn ] = 0;
        printf("Case #%d: %s\n",round+1,data);
   }
   return 0;
}