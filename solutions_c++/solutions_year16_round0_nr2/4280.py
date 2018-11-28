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
int dp[MAXN];

int main() {
    // freopen("B-large.in", "r", stdin);
    // freopen("outputb2.txt", "w", stdout);
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> s;
        zero(dp);
        if (s[0] == '+') dp[0] = 0; else dp[0] = 1;

        for (int i = 1; i < s.length(); i++) {
            if (s[i] == '+') dp[i] = dp[i - 1];
            else {
                if (s[i - 1] == '-') dp[i] = dp[i - 1];
                else dp[i] = dp[i - 1] + 2;
            }
        }
        cout << "Case #" << i << ": " << dp[s.length() - 1] << endl;
    }
    return 0;
}
