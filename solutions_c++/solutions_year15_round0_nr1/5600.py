#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

char m[100][100];

int main(void){

    int T;
    scanf("%d",&T);

    char num[2000];

    for(int r = 0;r < T;++r){
        int smax;
        int ans = 0;
        scanf("%d ",&smax);
        scanf("%s",num);

        // ����������Z���Ă����āA�W�����v���������琏�������΂���
        int s = 0;
        for(int i = 0;i <= smax;++i){
            // i �̂Ƃ��ɔ�[����������A i �l�K�v�B����Ȃ���Α����B
            if(num[i]-'0' && s < i){
                ans += i - s;
                s = i;
            }
            s += num[i]-'0';
            //printf("%d %d %d\n",s,num[i]-'0',ans);
        }

        printf("Case #%d: %d\n",r+1,ans);
    }

}
