#include <bits/stdc++.h>
#define F first
#define S second
using namespace std;

typedef long long ll;


int solve();
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //freopen("output.txt", "w", stdout);
    srand(time(0));
    int t;
    int i = 0;
    cin >> t;
    while(t--){
        ++i;
        int y = solve();
        cout << "Case #" << i << ": ";
        if(y >= 0)cout << y << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
#define many(x, y) v[y + x] + u[maxn + y - x]
#define mp(x, y) make_pair(x, y)

string h;
int r[1000];
int s = 0;
int k;
int ans;
int solve(){
    cin >> h >> k;
    s = 0;
    ans = 0;
    for(int i = 0; i < h.size(); ++i){
        if(i + k > h.size() && h[i] == '-'){
            //cerr << i << endl;
            return -1;
        }
        if(h[i] == '-'){
            ++ans;
            for(int j = i; j < i + k; ++j)
                if(h[j] == '-')h[j] = '+';
                else h[j] = '-';
        }
    }
    return ans;
}
