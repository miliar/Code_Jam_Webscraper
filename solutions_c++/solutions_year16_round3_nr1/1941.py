// Anve$hi $hukla
#include <bits/stdc++.h>
using namespace std;
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(NULL);}}$;

typedef long long LL;
const int Maxn = 200005;

void printVector(vector <string> &v) {
	for(auto x: v) {
		cout << " " << x;
	}
	cout << endl;
}
int main() {
	int tc;
	cin >> tc;
	for(int test = 1; test <= tc; test++) {
		int n;
		vector <string> ans;
		ans.clear();
		cin >> n;
		vector <int> p(n);
		for(int i = 0; i < n; i++) {
			cin >> p[i];
		}

		int s = accumulate(p.begin(), p.end(), 0);
		int t = (s) / 2;

		vector <pair <int, int> > v(n);
		
		for(int i = 0; i < n; i++) {
			v[i] = {p[i], i};
		}
		sort(v.rbegin(), v.rend());
		if(s % 2 == 1) {
			v[0].first--;
			string temp;
			temp += (char)('A' + v[0].second);
			ans.push_back(temp);
		}

 		for(int i = 0; i < t; i++) {
			sort(v.rbegin(), v.rend());
			string temp;
			if(v[1].first > 0) {
				temp += (char)('A' + v[0].second);
				temp += (char)('A' + v[1].second);
				v[0].first--;
				v[1].first--;
			} else {
				temp += (char)('A' + v[0].second);
				v[0].first--;
			}
			sort(v.rbegin(), v.rend());
			ans.push_back(temp);

		}
		cout << "Case #" << test << ":";
		printVector(ans);
	}	   
	return 0;
}
