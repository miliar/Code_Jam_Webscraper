#include <bits/stdc++.h>

#define itn itn
#define all(x) (x).begin(), (x).end()

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

void solve(){
	int n = nxt();
	cin.ignore();
	vector<vector<string> > a(n);
	vector<set<string> > S(n);
	for (int i = 0; i < n; i++){
		string s;
		getline(cin, s);
		a[i].push_back("");
		for (char c : s){
			if (c == ' '){
				a[i].push_back("");
			} else {
				a[i].back() += c;
			}
		}
	}

	set<string> words;
	for (int i = 0; i < n; i++){
		for (auto& x : a[i]){
			words.insert(x);
			S[i].insert(x);
		}
	}
	vector<int> ar;
	for (auto s : words){
		ar.push_back(0);
		for (int i = 0; i < n; i++)
			if (S[i].find(s) != S[i].end())
				ar.back() += (1 << i);
	}
	int N = (1 << (n - 2));
	int aa = 0;
	vector<int> ans(N);
	for (auto x : ar){
		int y = x & 3;
		x >>= 2;
		if (y == 3){
			aa++;
		} else if (y == 2){
			aa++;
			for (int i = 0; i < N; i++){
				if ((i & x) == 0)
					ans[i]--;
			}
		} else if (y == 1){
			aa++;
			for (int i = 0; i < N; i++){
				if ((i & x) == x)
					ans[i]--;
			}
		} else {
			for (int i = 0; i < N; i++){
				if ((i & x) < x && (i & x) > 0)
					ans[i]++;
			}
		}
	}
	printf("%d\n", aa + *min_element(all(ans)));
}

int main(){

	int T = nxt();
	for (int _ = 0; _ < T; _++){
		printf("Case #%d: ", _ + 1);
		solve();
		cerr << "Test #" << _ + 1 << " completed\n";
	}

	return 0;
}