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
  freopen("ans.txt", "w", stdout);
	int t; cin >> t;
	long long num;
	for(int i = 1; i <= t; i++){
		cin >> num;
		cout << "Case #" << i << ": ";
		if(num == 0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		
		set <int> digit;
		int mul = 1;
		while(digit.size() < 10){
			long long tmp = num * mul;
			while(tmp){
				digit.insert(tmp%10);
				tmp = tmp - tmp%10;
				tmp = tmp / 10;
			}
			mul = mul + 1;
		}

		cout << num * (mul - 1) << endl; 
	}
	return 0;
}
