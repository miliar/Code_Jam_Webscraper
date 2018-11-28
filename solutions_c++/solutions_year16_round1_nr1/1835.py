#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

typedef long long lld;

#define SIZE 100

#define IN freopen("A-large.in","r",stdin);
#define OUT freopen("A-large.out","w",stdout);

int T;

string solve(string s, int k, string best)
{
	if(k == s.size()) return best;

	// cout << k << " " << s[k] << " " << best << endl;

	if(k == 0) return solve(s, k+1, s.substr(0,1));

	string l = solve(s, k+1, s[k] + best);
	string r = solve(s, k+1, best + s[k]);
	if(l > r) {
		return l;
	} else {
		return r;
	}

}

int main()
{
	IN
	OUT
	int i,t;
	string S;

	cin >> T;
	cin.clear();
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	for(t=1;t<=T;t++){
		cin >> S;
		// cout << S << endl;
		
		string ans = S.substr(0, 1);

		for(i=1; i < S.size(); i++) {

			if(S[i] >= ans[0]) {
				ans = S.substr(i,1) + ans;
			} else {
				ans = ans + S.substr(i,1);
			}
		}

		// string ans = solve(S, 0, "");
		printf("Case #%d: ",t);
		cout << ans << endl;
	}
	return 0;
}
