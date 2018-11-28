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

#define GB(m, x) ((m) & (1<<(x)))
#define SB(m, x) ((m) |= (1<<(x)))
#define CB(m, x) ((m) &= ~(1<<(x)))
#define TB(m, x) ((m) ^= (1<<(x)))

using namespace std; typedef string string;
typedef unsigned long long ull; typedef long double ld;
typedef long long ll;         typedef pair<int, int> ii;
typedef pair<int, ii> iii;    typedef vector<int> vi;
typedef vector<ii> vii;       typedef vector<vi> vvi;
typedef vector<ll> vll;       typedef pair<string, string> ss;
const static int MX = 101001;


int main() {
	vector<pair<int, char> > Q;
	int n, i, j, a, b, t, tc = 1;
	char c, d;
	string ans;
	cin >> t;
	while(t--){
		ans = "";
		Q.clear();
		cin >> n;
		for(i = 0; i < n; i++){
			cin >> a;
			Q.push_back({a, 'A' + i});
		}
		sort(Q.begin(), Q.end(), greater<pair<int, char> >());
		if(Q.size() >= 2){
			c = Q[0].Y;
			while(Q[1].X < Q[0].X){
				ans.push_back(' ');
				ans.push_back(c);
				Q[0].X--;
			}
			sort(Q.begin(), Q.end(), greater<pair<int, char> >());
		}
		while(Q.size() >= 3){
			a = Q[2].X; c = Q[2].Y;
			Q.erase(Q.begin() + 2);
			sort(Q.begin(), Q.end(), greater<pair<int, char> >());
			
			while(a){
				ans.push_back(' ');
				ans.push_back(c);
				a--;
			}
		}
		if(Q.size() == 2){
			a = Q[1].X; c = Q[1].Y;
			b = Q[0].X; d = Q[0].Y;
			while(a && b){
				a--; b--;
				ans.push_back(' ');
				ans.push_back(c);
				ans.push_back(d);
			}
		} else if(Q.size() == 1){
			while(Q[0].X){
				Q[0].X--;
				ans.push_back(' ');
				ans.push_back(Q[0].Y);				
			}
		}
		cout << "Case #" << tc++ << ":" << ans << "\n";
	}
}
