#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n - 1)&n) + 1 : 0; }

int t, T, N;
int i, j, k, m, n, l;
int a[1005], v[1005], d[1005];

string S;
vector<string> NUM;

string remove(string s, string chars) {
    string res = s;

    for (char c : chars) {
        auto p = find(s.begin(), s.end(), c);
        s.erase(p);
    }
    return s;
}

string solve() {
    string res = "";

    i = 0;
    while (i < S.size()) {
        switch (S[i])
        {
        case 'Z': i = 0; res += "0"; S = remove(S, "ZERO"); break;
        case 'W': i = 0; res += "2"; S = remove(S, "TWO"); break;
        case 'U': i = 0; res += "4"; S = remove(S, "FOUR"); break;
        case 'X': i = 0; res += "6"; S = remove(S, "SIX"); break;
        case 'G': i = 0; res += "8"; S = remove(S, "EIGHT"); break;
        default:
            ++i;
        }
    }

    i = 0;
    while (i < S.size()) {
        switch (S[i])
        {
        case 'O': i = 0; res += "1"; S = remove(S, "ONE"); break;
        case 'T': i = 0; res += "3"; S = remove(S, "THREE"); break;
        case 'F': i = 0; res += "5"; S = remove(S, "FIVE"); break;
        case 'S': i = 0; res += "7"; S = remove(S, "SEVEN"); break;
        default:
            ++i;
        }
    }

    i = 0;
    while (i < S.size()) {
        switch (S[i])
        {
        case 'N':
        case 'E':
        case 'I': i = 0; res += "9"; S = remove(S, "NINE"); break;
        default:
            ++i;
        }
    }
    
    sort(res.begin(), res.end());
    return res;
}

int main() {
    //cout << remove("OZONETOWER", "ZERO") << endl;

    cin >> T;
    F1(t, T) {
        cin >> S;

        cout << "Case #" << t << ": " << solve() << endl;
    }

    //system("pause");
    return 0;
}
