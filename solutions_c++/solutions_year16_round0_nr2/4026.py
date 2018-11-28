#include <bits/stdc++.h>
using namespace std;

const int N = 110;

char s[N], tmp[N];

void flip(int i){
    for(int j = 1; j <= i; j++){
        tmp[j] = (s[j] == '+')? '-' : '+';
    }
    for(int j = 1; j <= i; j++){
        s[i - j + 1] = tmp[j];
    }
}

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int k = 1; k <= t; k++){
        scanf("%s", s + 1);
        int n = strlen(s + 1), ans = 0;
        for(int i = n; i >= 1; i--){
            if(s[i] == '-'){
                int j = 0;
                while(j < i && s[j + 1] == '+') j++;
                if(j > 0) flip(j), ans++;
                flip(i), ans++;
            }
        }
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}
