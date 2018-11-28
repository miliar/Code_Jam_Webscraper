#define _CRT_SECURE_NO_WARNINGS
#include <cctype>
#include <climits>
#include <cmath>
#include <cstring>
#include <deque>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <numeric>
#include <ratio>
#include <regex>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <valarray>

using namespace std;

#define sz(v) (int)v.size()
#define eps 1e-10
#define all(v) v.begin(), v.end() 
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define chk(a,k) ((bool)(a&(1<<(k))))
#define set0(a,k) (a&(~(1<<(k))))
#define set1(a,k) (a|(1<<(k)))
#define in(v, x) (find(all(v),x) != v.end()) 
#define re return
#define sum(v) accumulate(v.begin(),v.end(),(ld)0)
#define tr(v,it) for(auto it=v.begin();it != v.end();it++)
#define asrt(v) sort(v.begin(),v.end())
#define dsrt(v) sort(v.rbegin(),v.rend())
#define rev(v) reverse(v.begin(),v.end())
#define pi 3.1415926535897932384626433832795
#define MOD 1000000007
#define print(v) for (auto& i:v) cout<<i<<endl 
#define endl '\n'

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vi> vvi;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vi> vvi;

#define print "Case #"+to_string(t1)+": " 

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;

string res;

bool foo(int n, int p, int r, int s) {

	if (n == 2) {
		if (p == 1 && r == 1) {
			res = "PR";
			re 1;
		}
		else if (p == 1 && s == 1) {
			res = "PS";
			re 1;
		}
		else if (r == 1 && s == 1) {
			res = "RS";
			re 1;
		}
		else{
			re 0;
		}
	}

	if (n == 4)  {
		if (p == 2 && r == 1 && s == 1) {
			res = "S";
			re 1;
		}
		if (p == 1 && r == 2 && s == 1) {
			res = "P";
			re 1;
		}
		if (p == 1 && r == 1 && s == 2) {
			res = "R";
			re 1;
		}
		re 0;
	}
	else{
		int k = n / 4;
		if (r < k || p < k || s < k) re 0;
		re foo(n / 4, r-k, s-k, p-k);
	}

}

string calc(string s) {
	string r = "";
	int n = sz(s);
	if (sz(s) == 1) re s;
	string s1 = calc(s.substr(0, n / 2)), s2 = calc(s.substr(n / 2, n / 2));
	
	if (s1 < s2) {
		r += s1;
		r += s2;
		re r;
	}
	else{
		r += s2;
		r += s1;
		re r;
	}

}

void F(int t1) {
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	n = round(pow(2, n));
	cout << print;

	res = "";
	int q = foo(n, p, r, s);
	if (q == 0) {
		cout << "IMPOSSIBLE";
	}
	else{
		while (sz(res) != n) {
			string r = "";
			for (int i = 0; i < sz(res); i++) {
				if (res[i] == 'S') r += "PRPS";
				else if (res[i] == 'P') r += "PRRS";
				else r += "PSRS";
			}
			res = r;
		}
		cout << calc(res);
	}
	cout << endl;
}

int main() {
	freopen("Data/in.txt", "r", stdin);
	freopen("Data/out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t1 = 1; t1 <= T; t1++) {
		F(t1);
	}
	getchar();
	return 0;
}
