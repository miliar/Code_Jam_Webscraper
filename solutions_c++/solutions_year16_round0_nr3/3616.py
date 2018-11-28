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
#define MAXN 50
#define MAXM 1000
#define MOD 1000000007

int T, N, J;
int total = 0;
VI prime;
void make_prime() {
    for (int i = 2; i < 1000; i++) {
        bool flag = true;
        for (int j = 2; j < sqrt(i) + 1; j++) {
            if (i % j == 0) {
                flag = false;
                break;
            }
        }
        if (flag) prime.PB(i);
        if (prime.size() > 100) return;
    }
}

LL change(string s, int index) {
    LL ans = 0;
    for (int i = s.length() - 1; i >= 0; i--) ans += (s[i] - '0') * pow(index, s.length() - 1 - i);
    return ans;
}

void add_ans(string s) {
    cout << s << ' ';
    for (int i = 2; i <= 10; i++) {
        LL now = change(s, i);
        for (int j = 0; j < prime.size(); j++)  {
            if (now % prime[j] == 0) {
                cout << prime[j] << ' ';
                break;
            }
        }
    }
    cout << endl;
    ++total;
    if (total >= J) exit(0);
}


void dfs(string s) {
    if (s.length() == N) {
        for (int i = 2; i <= 10; i++) {
            LL now = change(s, i);
            bool flag = false;
            for (int j = 0; j < prime.size(); j++) {
                if (now % prime[j] == 0) flag = true;
            }
            if (!flag) return;
        }
        add_ans(s);
        return;
    }
    if (s.length() < N - 1) {
        dfs(s + '0');
        dfs(s + '1');
    } else
        dfs(s + '1');
}

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("outputc1.txt", "w", stdout);
    make_prime();
    cin >> T >> N >> J;
    cout << "Case #1:" << endl;
    dfs("1");
    return 0;
}
