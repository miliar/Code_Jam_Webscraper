#include <bits/stdc++.h>

using namespace std;


pair<string, int> solve(string str1, string str2) {
	string newStr = "";
	int res = 0, sz1 = (int)str1.size(), sz2 = (int)str2.size();
	int i = 0, j = 0;
	while(true) {
//		cout << i << ' ' << j << endl;
		if(i < sz1 && j < sz2 && str1[i] != str2[j]) {
			if(j > 0 && str1[i] == str2[j - 1]) res++, i++;
			else if(j > 0 && str2[j] == str2[j - 1]) res++, j++;
			else if(j < sz2 - 1 && str2[j] == str2[j + 1]) res++, j++;
			//else if(i < sz1 - 1 && str1[i] == str1[i + 1]) res++, i++;
			else return make_pair("", -1);
		} else if(i < sz1 && j < sz2 && str1[i] == str2[j]) {
			newStr += str1[i];
			i++, j++;
		} else if(i < sz1) {
			if(str1[i] == str1[i - 1]) res++, i++;
			else return make_pair("", -1);
		}	else if(j < sz2) {
			if(str2[j] == str2[j - 1]) res++, j++;
			else return make_pair("", -1);
		}
		if(i == sz1 && j == sz2) break;
	}
//	cout << newStr << endl;
//	cout << endl;
	return make_pair(newStr, res);
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, n, idx = 1, res, tmp;
	vector<string> v;
	pair<string, int> p;
	cin >> t;
	while(t--) {
		cin >> n;
		v.resize(n);
		res = -1;
		for(int i = 0; i < n; i++) cin >> v[i];
		for(int i = 0; i < n; i++) {
			tmp = 0;
			p.first = v[i];
			for(int j = 0; j < n; j++) {
				if(i == j) continue;
				p = solve(p.first, v[j]);
				tmp += p.second;
			}
			if(res == -1) res = tmp;
			else res = min(res, tmp);
		}
		cout << "Case #" << idx++ << ": ";
		if(res == -1) cout << "Fegla Won\n";
		else cout << res << endl;
	}

	return 0;
}
