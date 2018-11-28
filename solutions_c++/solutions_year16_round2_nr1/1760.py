#include <cstdio>
#include <cstring>

int T;
char s[3000];
int ct[300], ct2[300];

char word[10][30] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void minus(char c, int num){
    int cc = ct[c];
    ct2[num] += cc;
    int len = strlen(word[num]);
    for (int i = 0; i < len ;i++){
        ct[word[num][i]] -= cc;
    }
}

void solve(){
    scanf("%s", s);
    int len = strlen(s);
    memset(ct, 0, sizeof(ct));
    memset(ct2, 0, sizeof(ct2));
    for (int i = 0; i < len; i++){
        ct[s[i]]++;
    }
    minus('Z', 0);
    minus('W', 2);
    minus('X', 6);
    minus('G', 8);
    minus('S', 7);
    minus('V', 5);
    minus('H', 3);
    minus('U', 4);
    minus('O', 1);
    minus('E', 9);
    for (int i = 0; i <= 9; i++){
        for (int j = 0; j < ct2[i]; j++){
            printf("%d", i);
        }
    }
    printf("\n");
}

int main(){
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
