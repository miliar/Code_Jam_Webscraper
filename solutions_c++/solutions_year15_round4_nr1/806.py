#include<bits/stdc++.h>
#define rep(i, a, b) for(int i = (int)a; i < (int)b; i++)
#define red(i, a, b) for(int i = (int)a; i > (int)b; i--)
#define RED true
#define BLACK false
#define pb push_back
#define mk make_pair
#define fi first
#define se second
using namespace std;
typedef pair<int, int> ii;
typedef long long ll;
typedef pair<ii, int> iii;
typedef pair< pair<double, double>, double>  ddd;
typedef vector<int> vi;
const int N = 100 + 7;
const int M = N * 3;
const int inf = 1e9 + 7;
const int base = 1e9 + 9;
const double pi = acos(-1);
const double ep = 1e-15;

string s[N];
int dp[N][N];
int n, m;

bool cnt(int posx, int posy, char dir){
    if (dir == '<'){
        int tmp = dp[posx][posy-1] - dp[posx-1][posy-1];
        return tmp == (posy - 1);
    }
    if (dir == '^'){
        int tmp = dp[posx-1][posy] - dp[posx-1][posy-1];
        return tmp == (posx-1);
    }
    if (dir == '>'){
        int tmp = dp[posx][m] - dp[posx-1][m] - (dp[posx][posy] - dp[posx-1][posy]);
        return (tmp == m - posy);
    }
    if (dir == 'v'){
        int tmp = dp[n][posy] - dp[n][posy-1] - (dp[posx][posy] - dp[posx][posy-1]);
        return (tmp == n - posx);
    }
}

string x = "^>v<";

int main(){
    freopen("A-large (2).in" , "r", stdin);
    freopen("out.txt", "w", stdout);
    int test;
    cin >> test;
    rep(tt, 1, test + 1){
        scanf("%d%d\n", &n, &m);
        memset(dp, 0, sizeof(dp));
        int ans =0 ;
        bool kt = true;
        rep(i, 0, n)
            getline(cin, s[i]);
        rep(i, 0, n){
            rep(j, 0, m){
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j];
                if (s[i][j] == '.') dp[i+1][j+1] ++;
            }
        }
        rep(i, 0, n){
            rep(j, 0, m){
                if (s[i][j] != '.'){
                    if (cnt(i + 1, j + 1, s[i][j])){
                        ans++;
                        bool tmp = false;
                        rep(t, 0, 4)
                            if (!cnt(i+1, j+1, x[t])){
                                tmp = true;
                                break;
                            }
                        if (tmp == false){
                            kt = false;
                            break;
                        }
                    }
                }
            }
        }
        printf("Case #%d: ", tt);
        if (kt == false){
            cout<<"IMPOSSIBLE\n";
        }else cout<<ans<<endl;
    }
}
