#include <bits/stdc++.h>

using namespace std;

#define PB push_back
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define LL long long
#define sd(x) scanf("%d", &x)
#define sld(x) scanf("%lld", &x)
#define MOD 1000000007
#define SQ 112345
#define N 1123456
#define SZ(X) ((LL)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, A, B) for (LL I = A; I <= B; ++I)
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define PII pair<LL,LL>

int r, c;
string s[110];


int get(int x, int y){
    int i, j;
    for(i = 0; i < c; i++){
        if(i == y){
            continue;
        }
        if(s[x][i] != '.'){
            return 1;
        }
    }
    for(i = 0; i < r; i++){
        if(i == x) continue;
        if(s[i][y] != '.'){
            return 1;
        }
    }
    return 0;
}

int vali(int x, int y){
    if(x < 0 || x >= r || y < 0 || y >= c) return 0;
    return 1;
}

int reach(int x, int y){
    int dx, dy;
    if(s[x][y] == '<'){
        dy = -1;
        dx = 0;
    }
    if(s[x][y] == '>'){
        dy = 1;
        dx = 0;
    }
    if(s[x][y] == '^'){
        dy = 0;
        dx = -1;
    }
    if(s[x][y] == 'v'){
        dy = 0;
        dx = 1;
    }
    x += dx;
    y += dy;
    while(vali(x, y)){
        if(s[x][y] != '.'){
            return 1;
        }
        x += dx;
        y += dy;

    }
    return 0;
}

int solve(){
    cin>>r>>c;
    int i, j;
    for(i = 0; i < r; i++){
        cin>>s[i];
    }
    int ans = 0;
    for(i = 0; i < r; i++){
        for(j = 0; j < c; j++){
            if(s[i][j] != '.'){
                if(!get(i, j)){
                    cout<<"IMPOSSIBLE"<<endl;
                    return 0;
                }
                if(!reach(i, j)){
                    ans++;
                }
            }
        }
    }
    cout<<ans<<endl;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    LL t = 1;
    int o = 1;
    cin>>t;
    while(t--){
        printf("Case #%d: ", o++);
        solve();
    }
    return 0;
}
