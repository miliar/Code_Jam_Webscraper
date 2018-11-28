#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cctype>
#include<climits>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<fstream>
#include<deque>
#include<algorithm>
#include<numeric>
#include<utility>
#include<complex>
#include<memory>
#include<functional>

using namespace std;

#define all(g) (g).begin(),(g).end()
#define REP(i, x, n) for(int i = x; i < n; i++)
#define rep(i,n) REP(i,0,n)
#define F(i,j,k) fill(i[0],i[0]+j*j,k)
#define P(p) cout<<(p)<<endl;
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define INF (1<<28)
#define pb push_back

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long> vl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<long, long> pll;
typedef long long ll;

bool isOk(string a) {
	rep(i, a.size()) {
		if (a[i] == '-') return false;
	}
	return true;
}

void flip(string &a, int point) {
	string before = a.substr(0, point + 1);
	rep(i, point + 1) {
		if (before[i] == '+') {
			a[point - i] = '-';
		}
		else {
			a[point - i] = '+';
		}
	}
}
int main() {
	int T;
	cin >> T;
	ofstream output("B_large.txt");
	REP(i, 1, T + 1) {
		string a;
		cin >> a;
		int ans = 0;
		int n = a.length();
		int c, d;
		string b(n, '+');
		for (int j = n - 1; j >= 0; j--) {
			if (a[j] != b[j]) {
				flip(b, j);
				ans++;
			}
		}
		/*for (int j = n - 1; j >= 0; j--) {
			if (a[j] == '-') {
				if (a[0] == '-') {
					flip(a, j);
					ans++;
				}
				else {
					int k = 0;
					while (k >= 0 && k < n && a[k] == '+' && a[j - k] == '-') k++; 
					flip(a, k); ans++;
					flip(a, j); ans++;
				
				}
			}
		}*/
		output << "Case #" << i << ": " << ans << endl;
	}




	return 0;
}