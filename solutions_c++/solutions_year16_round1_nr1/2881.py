#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

typedef pair<int, int> PII;
typedef pair<pair<int, int>, int> triple;
typedef map<string, int> MSI;
typedef map<string, char> MSC;
typedef map<int, int> MII;
typedef map<char, int> MCI;
typedef map<PII, int> MPI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define fill(a) memset(a.begin(), a.end(), 0)
#define zero(a) memset(a, 0, sizeof(a))
#define MP make_pair
#define PB push_back
#define F first
#define S second
//-----------------------------
#define MAXN 1000
#define MAXM 1000
#define MOD 1000000007

int T;
string s;
string ans;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("outputA.txt", "w", stdout);
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> s;
        ans = s[0];
        for (int j = 1; j < s.length(); j++) {
            if (s[j] >= ans[0]) ans = s[j] + ans;
            else ans = ans + s[j];
        }
        cout << "Case #" << i << ": " + ans << endl;
    }
    return 0;
}
