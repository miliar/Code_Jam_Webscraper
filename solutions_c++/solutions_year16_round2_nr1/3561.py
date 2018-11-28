#include <bits/stdc++.h>

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> Pair;
typedef complex<double> Complex;

const double PI = M_PI;
const int INF = 1e9;

int a[32];
int l[10];
vector<string> Z = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE",
    "TEN"
};

string ans = "";

int valid() {
    for(int i = 0; i < 32; i++) {
        if(a[i] < 0) return -1;
    }

    for(int i = 0; i < 32; i++) {
        if(a[i] != 0) return 0;
    }

    return 1;
}
bool ok = false;;

void dfs(int p) {
    if(ok) return;
    int res = valid();
    if(res == 1) {
        ok = true;
        for(int i = 0; i < 10; i++) {
            for(int j = 0; j < l[i]; j++) {
                ans += (char)(i+'0');
            }
        }
        return ;
    }
    if(res < 0) return;
    if(p == 10) {
        return;
    }

    bool ok = true;

    dfs(p+1);
    for(int i = 0; i < Z[p].size(); i++) {
        int pos = Z[p][i] - 'A';
        a[pos]--;
    }
    l[p]++;
    dfs(p);
    dfs(p+1);
    for(int j = 0; j < Z[p].size(); j++) {
        int pos = Z[p][j] - 'A';
        a[pos]++;
    }
    l[p]--;
}

int main() {
    int N;
    cin >> N;
    for(int t = 1; t <= N; t++) {
        string s = "", w;
        memset(a, 0, sizeof a); 
        memset(l, 0, sizeof l);
        cin >> w;
        for(int i = 0; i < w.size(); i++) {
            int b = w[i] - 'A';
            a[b]++;
        }

        dfs(0);

        cout << "Case #" << t << ": " << ans << endl;
        ans = "";
        ok = false;
    }
}


