#include <bits/stdtr1c++.h>

#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl

using namespace std;

const unsigned long long base = 1925728309U;

int t, n;
unordered_map <unsigned long long, int> dp;
unordered_map <unsigned long long, bool> visited;

int F(vector <int> v){
    sort(v.begin(), v.end());

    unsigned long long h = 0;
    int i, j, k, x, n = v.size(), res = v[n - 1];
    for (i = 0; i < n; i++) h = (h * base) + v[i];
    if (visited[h]) return dp[h];

    for (i = 0; i < n; i++){
        x = v[i];
        if (x > 1){
            for (k = 1; k < x; k++){
                vector <int> temp;
                for (j = 0; j < i; j++) temp.push_back(v[j]);
                for (j = i + 1; j < n; j++) temp.push_back(v[j]);
                temp.push_back(k);
                temp.push_back(x - k);
                int z = 1 + F(temp);
                if (z < res) res = z;
            }
        }
    }

    visited[h] = true;
    return (dp[h] = res);
}

int main(){
    read();
    write();
    //freopen("test1.txt", "w", stdout);

    vector <int> v;
    int T = 0, i, j, k, x;

    scanf("%d", &t);
    while (t--){
        v.clear();
        scanf("%d", &n);
        for (i = 0; i < n; i++){
            scanf("%d", &x);
            v.push_back(x);
        }

        int res = F(v);
        printf("Case #%d: %d\n", ++T, res);
    }
    return 0;
}
