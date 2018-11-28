#include <bits/stdc++.h>

using namespace std;

#define REP(i, n)       for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i, n)      for(int i = (n)-1; i >= 0; i--)
#define FOR(i, a, b)    for(int i = (a), _b = (b); i <= _b; i++)
#define FORD(i, a, b)   for(int i = (a), _b = (b); i >= _b; i--)
#define FORALL(i, v)    for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector <int> vi;
typedef vector <ll> vll;

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
  int t; cin >> t;
	for(int i = 1; i <= t; i++){
		string inp; cin >> inp;
		int f = 0;
		if(inp[0] == '-') f = 1;
		else f = 0;
		for(int j = 1; j < (int) inp.size(); j++){
			if(inp[j] == '-' && inp[j] != inp[j-1]) f += 2;
		}
		cout << "Case #" << i << ": " << f << endl;
	}
	return 0;
}
