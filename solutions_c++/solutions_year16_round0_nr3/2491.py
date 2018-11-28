#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)
typedef long long lint;

struct JamCoin {
	vector< bool > seq;
	vector< int > div;
	
	void dump(int N) {
		for_(i,0,N) cout << seq[N - i - 1];
		cout << " ";
		for_(i,2,11) cout << div[i] << (i < 10 ? " " : "\n");
	}
};

lint pow(lint a, int x) {
	lint res = 1;
	
	while (x > 0) {
		if (x & 1) res *= a;
		a *= a;
		x >>= 1;
	}
	
	return res;
}

int calcDiv(int N, vector< bool >& s, int b) {
	lint x = 0;
	for_(i,0,N) if (s[i]) x += pow(b, i);
	
	int rep = (int)sqrt(x);
	for_(i,2,rep) {
		if (x % i == 0) return i;
	}
	
	return -1;
}

void solve() {
	int N, J;
	cin >> N >> J;
	
	vector< JamCoin > ans;
	
	for_(i,1,N-1) {
	for_(j,i+1,N-1) {
	for_(k,j+1,N-1) {
	for_(l,k+1,N-1) {
		vector< bool > s(N, 0);
		s[0] = s[N - 1] = 1;
		s[i] = s[j] = s[k] = s[l] = 1;
		
		bool flag = false;
		vector< int > div(11, -1);
		
		for_(i,1,6) {
			div[2 * i - 1] = 2;
			div[2 * i] = calcDiv(N, s, 2 * i);
			if (div[2 * i] == -1) {
				flag = true;
				break;
			}
		}
		
		if (!flag) ans.push_back(JamCoin{s, div});
		cerr << ans.size() << " ";
	}
	if ((int)ans.size() == J) break;
	}
	if ((int)ans.size() == J) break;
	}
	if ((int)ans.size() == J) break;
	}
	
	for_(i,0,J) ans[i].dump(N);
}

int main() {
	int T;
	cin >> T;
	
	for_(i,0,T) {
		cout << "Case #" << i + 1 << ":" << endl;
		solve();
	}
}