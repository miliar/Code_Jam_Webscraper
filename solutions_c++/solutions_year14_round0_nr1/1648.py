#include <bits/stdc++.h>
using namespace std;

int cnt[32];

void get_board(){
    int row; cin >> row;
    for(int i = 0; i < 16; i++){
        int num; cin >> num;
        if(i/4 == row-1) cnt[num]++;
    }
}

int main(){
    int t; cin >> t;
    for(int tc = 1; tc <= t; tc++){
        memset(cnt,0,sizeof(cnt));
        get_board();
        get_board();
        int ans = 0;
        for(int i = 1; i <= 16; i++){
            if(cnt[i] == 2) ans = ans? -1 : i;
        }
        printf("Case #%d: ",tc);
        if(ans > 0) printf("%d\n",ans);
        else puts(ans == 0 ? "Volunteer cheated!" : "Bad magician!");
    }
}

