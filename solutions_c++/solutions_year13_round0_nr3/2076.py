#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define MP make_pair
#define PB push_back
#define VI vector<int>
#define VS vector<string>
#define PII pair<int, int>
#define X first
#define Y second

int aabs(int a) { return (a<0)?-a:a; }
int mmax(int a, int b) { return (a>b)?a:b; }
int mmin(int a, int b) { return (a<b)?a:b; }

long long rev(long long x) {
	long long res=0;
	while(x > 0) {
		res = res*10 + (x%10);
		x /=10;
	}
	return res;
}

int digs(long long x) {
	int ans=0;
	while(x > 0) x/=10, ans++;
	return ans;
}

bool ispalindrome(long long x) {
	if(x < 10) return true;
	int d[18], dn=0;
	while(x > 0) d[dn++] = x%10, x/=10;
	for(int i=0; i<dn/2; i++) {
		if(d[i] != d[dn-1-i]) return false;
	}
	return true;
}

long long pot10[10];

int main(void)
{
	int T;
	long long A, B;

	pot10[0] = 1;
	for(int i=1; i<10; i++) pot10[i] = 10*pot10[i-1];
	
	cin >> T;
	for(int caso=0; caso<T; caso++) {
		cin >> A >> B;
		long long x = 1;

		int ans = 0;

		for(int i=1; i<10; i++) {
			if(ispalindrome(i*i) and i*i >= A and i*i <= B) ans++;
		}

		while(1) {
			long long k1 = x*pot10[digs(x)] + rev(x);
			long long k = k1*k1;
			if(ispalindrome(k) and k >= A and k <= B) {
				//cout << x*pot10[digs(x)] + rev(x) << endl;
				// cout << k << " " << k1 << endl;	
				ans++;
			} else if(k > B) {
				// cout << "Break: " << k << " " << B << endl;
				break;
			}

			for(int i=0; i<10; i++) {
				long long k1 = x*pot10[digs(x)+1] + i*pot10[digs(x)] + rev(x);
				long long k = k1*k1;
				if(ispalindrome(k) and k >= A and k <= B) {
					//cout << x*pot10[digs(x)+1] + i*pot10[digs(x)] + rev(x) << "\t" << k << endl;
					// cout << k << " " << k1 << endl;
					ans++;
				} 	else if(k > B) break;
			}
			x++;
		}

		// cout << "--- AB: " << A << " " << B << endl;
		// cout << "--- X: " << x << endl;
		cout << "Case #" << caso+1 << ": " << ans << endl;

	}
}
