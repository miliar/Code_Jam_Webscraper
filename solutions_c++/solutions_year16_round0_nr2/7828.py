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
const static int MAXN = 110;

int main() {
	//ios_base::sync_with_stdio(0); cin.tie(0);
	//cout<<fixed<<setprecision(9);
	int t, i, tc=1;
	string S;
	cin >> t;
	while(t--){
		cin >> S;
		S = string(S.rbegin(), S.rend());
		int r = 0, off = 0;
		for(i = 0; i < S.size();){
			if(S[i] == "-+"[off]) {
				r++;
				while(i < S.size() && S[i] == "-+"[off]){
					i++;
				}
				off ^= 1;
			} else i++;
		}
		cout << "Case #" << tc++ << ": " << r << endl;
	}
}
