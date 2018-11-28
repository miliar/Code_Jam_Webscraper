#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> iiii;
typedef pair<int, bool> ib;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

#ifdef __APPLE__
    ifstream fin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream fout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
#endif

int T;
string S;

int main() {
    fin >> T;
    for (int i = 1; i <= T; i++) {
        fin >> S;
        string ans = "";
        ans += S[0];
        for (int j = 1; j < S.length(); j++) {
            if (ans[0] <= S[j]) {
                ans = S[j] + ans;
            } else ans += S[j];
        }
        
        fout << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}