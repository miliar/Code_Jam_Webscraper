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
int cnt[100];
MCI cache;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> s;
        zero(cnt);
        cache.clear();
        for (int j = 0; j < s.length(); j++) cache[s[j]]++;
        cnt[0] = cache['Z'];
        cnt[2] = cache['W'];
        cnt[4] = cache['U'];
        cnt[6] = cache['X'];
        cnt[8] = cache['G'];
        cnt[3] = cache['H'] - cnt[8];
        cnt[5] = cache['F'] - cnt[4];
        cnt[1] = cache['O'] - cnt[0] - cnt[2] - cnt[4];
        cnt[7] = cache['V'] - cnt[5];
        cnt[9] = cache['I'] - cnt[8] - cnt[5] - cnt[6];
        string ans = "";
        for (int j = 0; j < 10; j++) {
            while (cnt[j]) {
                ans += char(j + '0');
                --cnt[j];
            }
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
