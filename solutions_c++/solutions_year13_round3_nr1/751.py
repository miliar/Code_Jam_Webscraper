#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

typedef long long ll;

char data[ 2000000 ];

int main(void){

    int T;
    scanf("%d",&T);

    for(int round = 0;round < T;++round){
        // �ǂݎ�����f�[�^���t����ǂށB
        // �q���A�������J�E���g����B�ꉹ�ɏo�������A�����͂O�ɂȂ�B
        // �v���A�����𒴂��Ă�����A��������A�������g�P�Ǝc��̕����������Z�B
        // ������������A���܂Ŕ��������A�q���ɂ�錻�ۃJ�E���g�̐ώZ�l�𑫂��B
        ll n;
        scanf("%s %lld",data,&n);
        ll slen = strlen(data);
        ll cc = 0;
        ll nvByCons = 0;
        ll ans = 0;
        for(ll z = 0;z < slen;++z){
            ll i = slen - 1 - z;
            bool isVow = false;
            switch(data[i])
            {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                isVow = true;
            }
            if( isVow ){
                // �ꉹ�ɏo����Ă��܂���
                cc = 0;
            }else{
                // �q���������B���b�L�[�B
                ++cc;
            }
            if( cc >= n ){
                // �����B��
                ll subans = z + 1 - (n - 1);
                ans += subans;
                nvByCons = subans;
            }else{
                // ����Ȃ��B
                // �ł����܂Ő����������̂�����΁A����𗘗p���邱�Ƃ��ł���B
                ans += nvByCons;
            }
        }
        printf("Case #%d: %lld\n",round+1,ans);
    }

    return 0;
}