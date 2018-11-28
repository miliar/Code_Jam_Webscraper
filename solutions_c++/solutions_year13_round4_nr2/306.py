// _temp.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll ans1, ans2;
ll n, p, N;

ll pw[100];

int main()
{
	int tc;
	pw[0] = 1;
	for(int i=1; i<=60; ++i) pw[i] = pw[i-1]*2;

	//freopen("a.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%i", &tc);
	for(int tt=1; tt<=tc; ++tt) {
		cin >> n >> p;
		N = pw[n];
		p = p - 1;
		// first
		//cout << N << endl;
		if (p + 1 == N) {
			ans1 =  N - 1;
		} else {
			for(int i=0; i<n; ++i) if  (((p >> (n-1-i)) & 1) == 0) {
				ans1 = pw[i+1] - 2;
				break;
			}
		}

		// second
		if (p==0) {
			ans2 = 0;
		} else 
			if (p==N-1) {
				ans2 = p;
			} else {
			ll mask = pw[n] - 1;
			for(int i=0; i<n; ++i) {
				mask = mask - pw[n-1-i];
				if (mask <= p) {
					ans2 = N - pw[i + 1];
					break;
				}				
			}
		}
		//printf("Case #%i: ", tt);
		cout << "Case #" << tt << ": ";
		cout << ans1 << " " << ans2 << endl;
	}
	return 0;
}

