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

string T;

int main() {
	int tc, t = 1;
	cin >> tc;
	while(tc--){
		cin >> T;
		string R = T.substr(0, 1);
		for(int i = 1; i < T.size(); i++){
			if(R[0] <= T[i]) R = T.substr(i, 1) + R;
			else R = R + T.substr(i, 1);
		}
		cout << "Case #" << t++ << ": " << R << endl;
	}
}
