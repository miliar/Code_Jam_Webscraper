#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>
#include <stack>
#include <queue>
#include <sstream>
#include <numeric>
#include <iterator>
using namespace std;

#define maX(a, b) ( (a) > (b) ? (a) : (b))
#define miN(a, b) ( (a) < (b) ? (a) : (b))
#define pb push_back
#define mp make_pair
#define fill(a, v) memset(a, v, sizeof a)
#define tr(v, it) for(typeof((v).begin()) it = (v).begin(); it != (v).end();it++)
#define sz(a) ((int)(a.size()))
#define ff first
#define ss second

const int INF = 1e9;
const double eps = 1e-9;
typedef long long lli;

lli gcd(lli a, lli b) { if(a == 0) return b; return gcd(b%a, a);}
lli exp(lli base, lli expo, lli m) { lli ans = 1;while(expo > 0) {ans = (ans * base) % m; expo >>= 1; base = (base * base) % m;} return ans;}

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("out1.txt", "w", stdout);

	int t;
	int smax;
	string str;
	lli cnt;

	cin >> t;
	for(int kase = 1;kase <= t;kase++) {
		cin >> smax;
		cin >> str;
		cnt = 0;
		lli tot = 0;

		for(int i = 0;i < str.length();i++) {
			int val = str[i]-'0';
			if(tot < i) {
				cnt += i-tot;
				tot += i-tot;
			}
			tot += val;
		}

		cout << "Case #" << kase << ": " << cnt << "\n";
	}

	return 0;
}









