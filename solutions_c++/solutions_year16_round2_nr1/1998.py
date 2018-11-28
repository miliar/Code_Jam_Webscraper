#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <string>
#define repd(i,a,b) for (int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repd(i,0,n)
#define all(x) (x).begin(),(x).end()
#define mod 1000000007
#define inf 2000000007
#define mp make_pair
#define pb push_back
typedef long long ll;
using namespace std;
template <typename T>
inline void output(T a, int p) {
    if(p) cout << fixed << setprecision(p)  << a << "\n";
    else cout << a << "\n";
}
// end of template

vector<string> S = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

template <typename T> inline void voutput(T &v){
    rep(i, v.size()){
        if (i) cout << " " << v[i];
        else cout << v[i];
    }
    cout << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    int N;
    cin >> N;
    rep(i, N) {
        vector<int> alp(26, 0);
        string s;
        cin >> s;
        rep(j, s.size()){
            alp[s[j] - 'A']++;
        }
        vector<int> num(10, 0);
        num[8] = alp['G' - 'A'];
        rep(j, S[8].size()){
            alp[S[8][j] - 'A'] -= num[8];
        }
        num[2] = alp['W' - 'A'];
        rep(j, S[2].size()){
            alp[S[2][j] - 'A'] -= num[2];
        }
        num[6] = alp['X' - 'A'];
        rep(j, S[6].size()){
            alp[S[6][j] - 'A'] -= num[6];
        }
        num[7] = alp['S' - 'A'];
        rep(j, S[7].size()){
            alp[S[7][j] - 'A'] -= num[7];
        }
        num[3] = alp['T' - 'A'];
        rep(j, S[3].size()){
            alp[S[3][j] - 'A'] -= num[3];
        }
        num[5] = alp['V' - 'A'];
        rep(j, S[5].size()){
            alp[S[5][j] - 'A'] -= num[5];
        }
        num[9] = alp['I' - 'A'];
        rep(j, S[9].size()){
            alp[S[9][j] - 'A'] -= num[9];
        }
        num[4] = alp['U' - 'A'];
        rep(j, S[4].size()){
            alp[S[4][j] - 'A'] -= num[4];
        }
        num[0] = alp['Z' - 'A'];
        rep(j, S[0].size()){
            alp[S[0][j] - 'A'] -= num[0];
        }
        num[1] = alp['O' - 'A'];
        rep(j, S[1].size()){
            alp[S[1][j] - 'A'] -= num[1];
        }
        
        string ret = "";
        rep(j, 10){
            rep(k, num[j]){
                ret += ('0' + j);
            }
        }
        cout << "Case #" << i + 1 << ": ";
        output(ret, 0);
        
//        voutput(alp);
        
    }
    
    return 0;
}