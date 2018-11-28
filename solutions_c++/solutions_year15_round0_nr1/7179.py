#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
vector<string> vs;
string s;

int main() {
	int T, smax, sum, res;
	cin >> T;
	FOR(t, 1, T) {
		cin >> smax;
		cin >> s;
		res = sum = 0;
		FOR(i, 0, s.size()-1) {
			if(sum < i) {
				res += (i - sum);
				sum = i;
			} 
			sum += (s[i] - '0');
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}