#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char str[3000];
int num[30];
int ans[3000];
int cnt;
int temp[30];
bool judge(char c) {
    if(temp[c-'A'] > 0)return 1;
    return 0;
}

void jian(char s[]) {
    int len = strlen(s);
    for(int i = 0; i < len; i++) {
        temp[s[i] - 'A']--;
    }
}
bool jj(int a[]) {
    for(int i = 0; i < 26; i++) {
        if(a[i] != 0)return 0;
    }
    return 1;
}

void fun(int n)
{
    if(n == 1)
    {
        while(judge('O') && judge('N')&& judge('E')) {
                ans[cnt++] = 1;
                jian("ONE\0");
        }
    } else if(n == 2) {
        while(judge('T') && judge('W')&& judge('O')) {
                ans[cnt++] = 2;
                jian("TWO\0");
            }
    } else if(n == 4)
    {
        while(judge('F') && judge('O')&& judge('U') && judge('R')) {
            ans[cnt++] = 4;
            jian("FOUR\0");
        }
    }else if(n == 6) {
        while(judge('S') && judge('I')&& judge('X')) {
            ans[cnt++] = 6;
            jian("SIX\0");
        }
    }else if(n == 0) {
        while(judge('Z') && judge('E')&& judge('R') && judge('O')) {
            ans[cnt++] = 0;
            jian("ZERO\0");
        }
    }else if(n == 5){
        while(judge('F') && judge('I')&& judge('E') && judge('V')) {
            ans[cnt++] = 5;
            jian("FIVE\0");
        }
    }else if(n == 8){
        while(judge('E') && judge('I')&& judge('G') && judge('H') && judge('T')) {
            ans[cnt++] = 8;
            jian("EIGHT\0");
        }
    }else if(n == 9){
        while(num['N'-'A']>=2&& judge('E') && judge('I')) {
            ans[cnt++] = 9;
            jian("NINE\0");
        }
    }else if(n == 3){
        while(judge('T') && judge('H')&& num['E'-'A']>=2 && judge('R')) {
            ans[cnt++] = 3;
            jian("THREE\0");
        }
    }else if(n == 7){
        while(judge('S') && judge('V')&& num['E'-'A']>=2 && judge('N')) {
            ans[cnt++] = 7;
            jian("SEVEN\0");
        }
    }
}
bool solve(int a[])
{
    cnt = 0;

    for(int i = 0; i < 26; i++)
    {
        temp[i] = num[i];
    }
    for(int i = 0; i <= 9; i++)
    {
        int x = a[i];
        fun(x);
    }
    return jj(temp);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca = 1; ca <= t; ca++) {
        scanf("%s",str);
        int len = strlen(str);
        memset(num, 0, sizeof(num));
        for(int i = 0; i < len; i++){
            num[str[i] - 'A']++;
        }
        int a[11];
        for(int i = 0; i <= 9; i++){
            a[i] = i;
        }
        do {
            if(solve(a))
            {
                printf("Case #%d: ",ca);
                sort(ans,ans+cnt);
                for(int i = 0; i < cnt; i++) {
                    printf("%d",ans[i]);
                }
                printf("\n");
                break;
            }
        }while(next_permutation(a,a+10));
    }
    return 0;
}
