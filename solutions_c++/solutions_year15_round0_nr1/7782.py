/*
Google Code Jam 2015 Qualification Round
Problem A. Standing Ovation
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#define MAX 1003

char str[MAX]={0};
int strint[MAX]={0};
int strsum[MAX]={0};

int fun(int i, int s, int &j){
    int ans;
    while(i<=s){
        if(strint[i] == 0)
            break;
        i++;
    }
    j = i;
    while(j<=s){
        if(strint[j] != 0)
            break;
        j++;
    }
    //   i  j
    // 012345678
    // 210001000
    ans = j - strsum[j>0?j-1:0];
    if(ans < 0) ans = 0;
    return ans;
}

int main(){
    int tt,tests;
    scanf("%d", &tests);
    for(tt=1;tt<=tests;tt++){
        int s, ans, i, j;
        for(i=0;i<MAX;i++)
            str[i]=strint[i]=strsum[i]=0;
        scanf("%d", &s);
        scanf("%s", str);
        for(i=0;i<=s;i++){
            strint[i] = str[i] - '0';
            strsum[i] = strsum[i>0 ? i-1 : 0] + strint[i];
        }
        ans = 0;
        j = 0;
        while(j<s){
            int tmp = fun(j, s, j);
            if(ans<tmp) ans = tmp;
        }
        printf("Case #%d: %d\n", tt, ans);
    }
}
