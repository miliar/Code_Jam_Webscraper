/*************************************************************************
	> File Name: a.cpp
	> Author: BMan
	> Mail: luo-kai-jia@163.com
	> Created Time: 2016年05月01日 星期日 00时15分19秒
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;


char s[2222];


int cnt[256];


int digit_cnt[10];



int main() {
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++) {
        scanf("%s", s);

        memset(cnt, 0, sizeof(cnt));
        memset(digit_cnt, 0, sizeof(digit_cnt));
        
        for (int i = 0; s[i] != '\0'; i++) {
            cnt[s[i]]++;
        }

        // zero
        
        int c = cnt['Z'];
        digit_cnt[0] = c;
        cnt['Z'] -= c;
        cnt['E'] -= c;
        cnt['R'] -= c;
        cnt['O'] -= c;

        //six 
        //
        
        c = cnt['X'];
        digit_cnt[6] = c;
        cnt['S'] -= c;
        cnt['I'] -= c;
        cnt['X'] -= c;

        //seven
        c = cnt['S'];
        digit_cnt[7] = c;
        cnt['S'] -= c;
        cnt['E'] -= 2 * c;
        cnt['V'] -= c;
        cnt['N'] -= c;

        //five
        //
        c = cnt['V'];
        digit_cnt[5] = c;
        cnt['F'] -= c;
        cnt['I'] -= c;
        cnt['V'] -= c;
        cnt['E'] -= c;

        // four
        c = cnt['F'];
        digit_cnt[4] = c;
        cnt['F'] -= c;
        cnt['O'] -= c;
        cnt['U'] -= c;
        cnt['R'] -= c;

        //two 
        //
        c = cnt['W'];
        digit_cnt[2] = c;
        cnt['T'] -= c;
        cnt['W'] -= c;
        cnt['O'] -= c;
    
        //one 
        c = cnt['O'];
        digit_cnt[1] = c;
        cnt['O'] -= c;
        cnt['N'] -= c;
        cnt['E'] -= c;
        
        //nine 
        c = cnt['N'] / 2;
        digit_cnt[9] = c;
        cnt['N'] -= 2 * c;
        cnt['I'] -= c;
        cnt['E'] -= c;

        //eight 
        
        c = cnt['G'];
        digit_cnt[8] = c;
        cnt['E'] -= c;
        cnt['I'] -= c;
        cnt['G'] -= c;
        cnt['H'] -= c;
        cnt['T'] -= c;

        //three 
        c = cnt['T'];
        digit_cnt[3] = c;
        cnt['T'] -= c;
        cnt['H'] -= c;
        cnt['R'] -= c;
        cnt['E'] -= 2 * c;

        for (int i = 'A'; i <= 'Z'; i++) {
            if (cnt[i] != 0) {
                printf("ERROR\n");

            }
        }
        
        printf("Case #%d: ", _t);
        for (int i = 0; i <= 9; i++) {
            for(int c = 1; c <= digit_cnt[i]; c++)
                printf("%d", i);
        }
        printf("\n");
    }
    return 0;
}
