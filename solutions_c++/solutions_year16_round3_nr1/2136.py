#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef long double ldb;

#define fi first
#define se second
#define sz(x) x.size()
#define pb push_back
#define mkp make_pair
#define all(v) (v).begin(),(v).end()
#define forn(i,a,n) for(int i = a; i < n; i++)
#define dbg(a) cout << #a << " = " << a << endl

int n;

bool check(vector<int> v, int p, int s) {
	v[p]--;
	for(int i = 0; i < n; i++) {
		double k = (double) v[i] / (s);
		if(k > 0.5) {
			return false;
		} 
	}
	return true;
}

bool check(vector<int> v, int p, int q, int s) {
	v[p]--; v[q]--;
	
	for(int i = 0; i < n; i++) {
		double k = (double) v[i] / (s);
		if(k > 0.5) {
			return false;
		} 
	}
	return true;
}

void solve(int test){
	cout << "Case #" << test << ": ";
	cin >> n;
	vector<int> a(n);
	int sum= 0;
	for(int i = 0; i < n; i++) {
		cin >> a[i];
		sum += a[i];
	}
	string tmp = "";
	while(sum > 0) {
		outer : 
		for(int i = 0; i < n; i++) {
			for(int j = 0; j <= n; j++) {
				if(j == n) {
					if(a[i] > 0 && check(a, i, sum-1)) {
						a[i]--;
						sum--;
						char ch = i + 'A';
						cout << ch << " ";
						goto outer;
					}
				}
				else if(j == i) {
					if(a[i] > 1 && check(a, i, j, sum-2)) {
						a[i]-=2;
						sum-=2;
						char ch = i + 'A';
						cout << ch << ch << " ";
						goto outer;
					}
				}
				else  {
					if(a[i] > 0 && a[j] > 0 && check(a, i, j, sum-2)) {
						a[i]--;
						a[j]--;
						sum-=2;
						char ch = i + 'A';
						char ch1 = j + 'A';
						cout << ch << ch1 << " ";
						goto outer;
					}
				}
			}
		}
	cout << " ";
	}
	
	a.clear();
	cout << endl;
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int p;
	cin >> p;
	for(int i = 1; i <= p; i++) {
		solve(i);
	}

	return 0;
}


