#include <bits/stdc++.h>
#define pb push_back

using namespace std;

int t;

int main () {
	ios_base::sync_with_stdio(0);

	cin >> t;
	int caso = 1;
	while(t--){
		string s;
		cin >> s;
		int ans = 0;
		int pos = 0;
		int cost = 1;
		int i = 0;

		while(i < s.size()){
			bool ok = false;
			bool neg = false;

			while(i < s.size() && s[i] == '-'){
				i++;
				neg = true;
			}

			if(neg)
				ans += cost;
			
			while(i < s.size() && s[i] == '+'){
				i++;
				ok = true;
			}
			if(ok) cost = 2;
		}
		cout << "Case #"<<caso++<<": ";
		cout << ans << endl;
	}

	return 0;
}
