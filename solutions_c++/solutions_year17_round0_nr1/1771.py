#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long int ll;

const int MAXSIZE = 100;
const int INF = 2000*1000*1000;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie();

	int T;
	cin >> T;
	for(int t=1; t<=T; ++t) {
		string s;
		int k;
		cin >> s >> k;

		int ans = 0;
		for(size_t i=0; i+k-1 < s.length(); ++i)
			if (s[i] == '-') {
				for(size_t j=i; j<i+k; j++)
					s[j] = s[j]=='+'? '-':'+'; 
				ans++;
			}
		for(size_t i=s.length()-k; i<s.length(); ++i)
			if (s[i] == '-') ans = -1;

		if (ans != -1) {
			cout << "Case #" << t << ": " << ans;
		} else {
			cout << "Case #" << t << ": " << "IMPOSSIBLE";
		}
		if (t != T) cout << endl;
	}

	return 0;
}