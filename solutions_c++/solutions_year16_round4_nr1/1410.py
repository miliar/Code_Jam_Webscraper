#include<bits/stdc++.h>
using namespace std;
int n;
string str[14][3];
int dp[14][3][3];

bool win(int a, int b){
    if((a+1)%3 == b) return true;
    return false;
}

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.out", "w", stdout);
    str[0][0] = "S";    str[0][1] = "P";    str[0][2] = "R";
    for(int i = 1; i <= 12; i++){
        for(int j = 0; j < 3; j++){
            for(int k = 0; k < 3; k++){
                if(win(j, k)){
                    str[i][j] = (str[i-1][j] < str[i-1][k] ? str[i-1][j]+str[i-1][k]: str[i-1][k] +str[i-1][j]);
                }
            }
           // cout<<str[i][j]<<endl;
        }



    }
    dp[0][0][0] = dp[0][1][1] = dp[0][2][2] = 1;
    for(int i = 1; i <= 12; i++){
        for(int j = 0; j < 3; j++){
            for(int k = 0; k < 3; k++){
                if(!win(j, k)) continue;
                dp[i][j][0] = dp[i-1][j][0] + dp[i-1][k][0];
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][k][1];
                dp[i][j][2] = dp[i-1][j][2] + dp[i-1][k][2];
            }
        }
    }

    int tc, TC, n, s, p, r;
    scanf("%d", &TC);
    int i;
    for(tc = 1; tc <= TC; tc++){
        scanf("%d%d%d%d", &n, &r, &p, &s);

        cout <<"Case #"<<tc <<": " ;
        for(i = 0; i < 3; i++){
            if(dp[n][i][0] == s && dp[n][i][1] == p && dp[n][i][2] == r){
                cout << str[n][i] <<endl;
                break;
            }
        }
        if(i == 3) cout << "IMPOSSIBLE"<<endl;
    }
    return 0;
}
