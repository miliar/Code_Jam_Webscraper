#include <bits/stdc++.h>
#define EPS 1e-11
#define LB 1e11
#define EL cerr << endl;
#define DB(x) cerr << "#" << (#x) << ": " << (x) << " ";
#define DBL(x) cerr << "#" << (#x) << ": " << (x) << endl;
#define PR(x) cout << (x) << endl

#define X first
#define Y second
#define PB push_back
#define SQ(x) ((x)*(x)) 

using namespace std; typedef string string;
typedef unsigned long long ull; typedef long double ld;
typedef long long ll;         typedef pair<int, int> ii;
typedef pair<int, ii> iii;    typedef vector<int> vi;
typedef vector<ii> vii;       typedef vector<vi> vvi;
typedef vector<ll> vll;       typedef pair<string, string> ss;
const static int MX = 1010;

inline bool fits(string S, int x){
	string N = ""; int cc = S.size();
	while(cc--){
		N.push_back('0' + x%10);
		x /= 10;
	}
	if(x) return false;
	N = string(N.rbegin(), N.rend());
	for(int i = 0; i < S.size(); i++){
		if(S[i] != N[i] && S[i] != '?') return false;
	}
	return true;
}

inline bool cmp(int ma, int mb, int a, int b){
	if(abs(ma - mb) != abs(a - b)) return abs(ma - mb) > abs(a - b);
	if(ma != a) return ma > a;
	return mb > b;
}

int main() {
	int tc, i, j, t = 1, n;
	//string T = "?9?";
	//while(cin >> n) cout << fits(T, n) << endl;
	cin >> tc;
	while(tc--){
		string A, B;
		cin >> A >> B;
		int ma = 1011, mb = 1001011, n = A.size();
		for(int a = 0; a < 1000; a++) if(fits(A, a)){
			for(int b = 0; b < 1000; b++) if(fits(B, b)){
				if(cmp(ma, mb, a, b)){
					ma = a; mb = b;
				}
			}
		}
		cout << "Case #" << (t++) << ": " << setfill('0') << setw(n) << right << ma << " " << setfill('0') << setw(n) << right << mb << endl;
	}
	
}
