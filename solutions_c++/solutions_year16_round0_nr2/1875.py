#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iomanip>
#include <queue>
#include <utility>
#include <stack>
#include <ctime>

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define forn(i,n) for (i = 0; i < n; i++)

using namespace std;

typedef pair <int, int> pii;
typedef long double ld;
typedef long long ll;

const ld EPS = 1e-9;
const int INF = (int) 1e9;
const int N = (int) 1e3 + 5;
const ll M = (int) 1e9 + 7;

string rev(string s, int pos) {
    for (int i = 0; i <= pos; i++)
        if (s[i] == '+')
            s[i] = '-';
        else
            s[i] = '+';

    return s;
}

int solve(string s) {
    int n = s.length(), step = 0;
    bool flag = 1;
    while(flag) {
        flag = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '-') {
                s = rev(s, i);
                step++;
                flag = 1;
                break;
            }
        }
    }
    return step;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string s;
        cin >> s;
        cout << "Case #" << t + 1 << ": ";
        cout << solve(s) << endl;
    }
	return 0;
}
