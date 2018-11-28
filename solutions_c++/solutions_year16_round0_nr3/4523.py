#define _CRT_SECURE_NO_WARNINGS
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())


//‘f””»’è O(ãn)
long long  divisor(long long n) {
	if (n <= 1)return -1;
	for (long long i = 2; i*i <= n; i++)
		if (n%i == 0)return i;
	return -1;
}



long long to_i(string &s,int base) {
	long long res = 0;
	for (int i = 0; i<s.size(); i++)res = res * base + s[i] - '0';
	return res;
}
string to_s(int n,int base) {
	string s;
	do { s += n % base + '0'; n /= base; } while (n);
	reverse(s.begin(), s.end());
	return s;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	rep(tcase, t) {
		int N, J;
		cin >> N >> J;

		cout << "Case #" << tcase + 1 << ":" << endl;

		for (long long i = 1LL<<(N-1)|1; i < (1LL << N); i+=2) {
			string s = to_s(i,2);
			bool ok = true;
			long long div[11];
			for (int b = 2; b <= 10;b++) {
				long long m = to_i(s,b),d;
				d = divisor(m);
				div[b] = d;
				if (d == -1) {
					ok = false;
					break;
				}
			}
			if (ok) {
				/*for (int b = 2; b <= 10; b++) {
					long long m = to_i(s, b), d;
					cout << ' ' << m;
				}cout << endl;
				for (int b = 2; b <= 10; b++) {
					long long m = to_i(s, b), d;
					cout << ' ' << m%div[b];
				}cout << endl;*/

				cout<< to_s(i, 2);
				for (int b = 2; b <= 10; b++) {
					cout << ' ' << div[b];
				}
				cout << endl;
				if (--J == 0)break;
			}
		}
	}
	return 0;
}