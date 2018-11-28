#include <cstdio>
#include <iostream>
#include <algorithm>
#define N 1100
using namespace std;

char ch[N];

int main(){
    int t, s;
    scanf("%d", &t);
    for(int di = 1; di <= t; di++){
        scanf("%d", &s);
        scanf(" %s", ch);
        int len = s + 1;
        int ans = 0;
        int sum = ch[0] - '0';
        for(int i = 1; i < len; i++){
            if(ch[i] == '0') continue;
            else if(i <= sum) sum += ch[i] - '0';
            else{
                int temp = i - sum;
                ans += temp;
                sum += (ch[i] - '0' + temp);
            }
        }
        printf("Case #%d: %d\n", di, ans);
    }
    return 0;
}

