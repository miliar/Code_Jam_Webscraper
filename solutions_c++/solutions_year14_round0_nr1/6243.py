#include <bits/stdc++.h>

using namespace std;

int T;
int a, b;
int c1[5][5], c2[5][5];
int cc[17];

void solve(){
    int cnt = 0, ans;
    memset(cc, 0, sizeof(cc));
    for(int i = 0; i < 4; ++i){
        ++cc[c1[a][i]];
        ++cc[c2[b][i]];
    }
    for(int i = 1; i <= 16; ++i){
        if(cc[i] == 2){
            ++cnt;
            ans = i;
        }
    }
    if(cnt == 1)
        printf("%d\n", ans);
    else if(!cnt)
        printf("Volunteer cheated!\n");
    else
        printf("Bad magician!\n");
}

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(int s = 1; s <= T; ++s){
        scanf("%d", &a);
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                scanf("%d", &c1[i][j]);
        scanf("%d", &b);
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                scanf("%d", &c2[i][j]);
        --a;
        --b;
        printf("Case #%d: ", s);
        solve();
    }
    return 0;
}
