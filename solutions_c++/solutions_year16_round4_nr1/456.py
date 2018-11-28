#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>
#include<map>
#include<ctime>
#include<cstdio>

 
using namespace std; 
 
typedef long long ll; 
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
const long double PI = 3.14159265358979323846;  
const long double gammama = 0.57721566490153286060;
//const long double eps = 1e-5;
//const int INF = 50000;
const int N = 12;

//ll mod = 1000000009;

vector<string> sp, sr, ss;

void init() {
    sp.resize(N + 1);
    sr.resize(N + 1);
    ss.resize(N + 1);
    sp[0] = "P";
    sr[0] = "R";
    ss[0] = "S";
    for (int i = 0; i < N; ++i) {
        sp[i + 1] = sp[i] + sr[i];
        sr[i + 1] = ss[i] + sr[i];
        ss[i + 1] = sp[i] + ss[i];
    }
    for (int i = 1; i <= N; ++i) {
        for (int sh = 1; sh < ss[i].size(); sh *= 2) {
            for (int j = 0; j < ss[i].size(); j += 2 * sh) {
                if (ss[i].substr(j, sh) > ss[i].substr(j + sh, sh)) {
                    for (int k = j; k < j + sh; ++k)
                        swap(ss[i][k], ss[i][k + sh]);
                }
                if (sp[i].substr(j, sh) > sp[i].substr(j + sh, sh)) {
                    for (int k = j; k < j + sh; ++k)
                        swap(sp[i][k], sp[i][k + sh]);
                }
                if (sr[i].substr(j, sh) > sr[i].substr(j + sh, sh)) {
                    for (int k = j; k < j + sh; ++k)
                        swap(sr[i][k], sr[i][k + sh]);
                }
            }
        }
    }
    
}

bool ok(const string& str, int p, int r, int s) {
    int pp = 0, ss = 0, rr = 0;
    for (int i = 0; i < str.size(); ++i) {
        if (str[i] == 'P')
            ++pp;
        if (str[i] == 'R')
            ++rr;
        if (str[i] == 'S')
            ++ss;
    }
    return (pp == p) && (ss == s) && (rr == r);
}

string solve() {
    int n;
    int p, r, s;
    cin >> n >> r >> p >> s;
    string res = "IMPOSSIBLE";
    if (ok(sp[n], p, r, s))
        res = sp[n];
    if ((ok(ss[n], p, r, s)) && ((ss[n] < res) || (res[0] == 'I')))
        res = ss[n];
    if ((ok(sr[n], p, r, s)) && ((sr[n] < res) || (res[0] == 'I')))
        res = sr[n];
    return res;
    
}

int main() {
    init();
	//freopen("A-small.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int tt;
	//scanf("%d\n", &tt);
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
		cout << "Case #" << i + 1 << ": " << solve() << endl;
		std::cerr << i << endl;
	}
	return 0;
}