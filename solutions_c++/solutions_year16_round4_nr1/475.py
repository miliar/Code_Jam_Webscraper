#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int t, n, r[3];
string ans;
vector <char> cur;
char a[3] = {'R', 'P', 'S'};

int id(char c) {
    for (int i = 0; i < 3; i++)
        if (a[i] == c) return i;
    return -1;
}

string get(char c) {
    string result = "";
    result += c;
    int sz = (1 << n);
    while (result.size() < sz) {
        string temp = "";
        for (int i = 0; i < result.size(); i++) {
            char c = result[i];
            if (c == 'R') {
                temp += "RS";
            } else if (c == 'P') {
                temp += "PR";
            } else temp += "SP";
        }
        result = temp;
    }
    return result;
}

string srt(string s) {
    for (int i = 0; i < n; i++) {
        int sz = (1 << i);
        string t = "";
        for (int j = 0; j < (1 << n); j += 2 * sz) {
            string a = s.substr(j, sz);
            string b = s.substr(j + sz, sz);
            if (a > b) swap(a, b);
            t += a;
            t += b;
        }
        s = t;
    }
    return s;
}

void solve(int num) {
    scanf("%d", &n);
    for (int i = 0; i < 3; i++) scanf("%d", r + i);
    ans = "IMPOSSIBLE";
    for (int i = 0; i < 3; i++) {
        string s = get(a[i]);
        int rr[3] = {0, 0, 0};
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == 'R') rr[0]++;
            else if (s[j] == 'P') rr[1]++;
            else rr[2]++;
        }
        if (r[0] == rr[0] && r[1] == rr[1] && r[2] == rr[2]) {
            if (ans == "IMPOSSIBLE") {
                ans = srt(s);
            } else {
                ans = min(ans, srt(s));
            }
        }
    }
    cout << "Case #" << num << ": " << ans << endl;
}

int main(){

    scanf("%d", &t);

    for (int i = 1; i <= t; i++)
        solve(i);

    return 0;
}
