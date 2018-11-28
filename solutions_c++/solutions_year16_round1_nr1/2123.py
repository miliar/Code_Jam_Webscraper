#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define pp pair<int, int>
#define fi first
#define se second
#define esp 1e-9
#define inf 1000000001
#define mod 1000000007
#define N 2222
#define M 15
typedef long long ll;
typedef long double ld;
using namespace std;
int nt;
string s;

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> nt;
    for (int  kk = 1; kk <= nt; kk++) {
        cin >> s;
        string ret = "";
        ret = ret + s[0];
        for (int i = 1; i < s.size(); i++)
            if (s[i] >= ret[0])
                ret = s[i] + ret;
            else
                ret = ret + s[i];

        cout << "Case #" << kk << ": " << ret << "\n";
    }
    /**/return 0;
}
