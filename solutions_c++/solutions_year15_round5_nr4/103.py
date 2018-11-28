#include <bits/stdc++.h>

#define itn itn
#define all(x) (x).begin(), (x).end()
#define x first
#define y second

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

inline long long nxtll(){
	long long x;
	scanf("%lld", &x);
	return x;
}

void solve(){
	int p = nxt();
	vector<long long> e(p), f(p);
	for (int i = 0; i < p; i++)
		e[i] = nxtll();
	for (int i = 0; i < p; i++)
		f[i] = nxtll();
	vector<long long> al;
	for (int i = 0; i < p; i++)
		for (int j = 0; j < f[i]; j++)
			al.push_back(e[i]);
	multiset<long long> cur;
	vector<int> qw;
	cur.insert(0);
	qw.push_back(0);
	vector<long long> ans;
	int N = al.size();
	for (int i = 0; i < N; i++){
		if (!cur.empty() && *(cur.begin()) == al[i]){
			cur.erase(cur.begin());
		} else {
			ans.push_back(al[i]);
			for (int j = qw.size() - 1; j >= 0; j--){
				cur.insert(qw[j] + al[i]);
				qw.push_back(qw[j] + al[i]);
			}
			cur.erase(cur.begin());
		}
	}
	for (auto x : ans)
		printf("%lld ", x);
	puts("");
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