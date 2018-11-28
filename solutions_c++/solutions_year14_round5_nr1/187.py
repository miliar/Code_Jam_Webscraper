#include<iostream>
#include<iomanip>
using namespace std;

long long supto[1000001];

int main() {
	cin.sync_with_stdio(false);
	int t;
	cin >> t;
	
	for(int TCASE = 0; TCASE < t; TCASE ++ ) {
		int n, p, q, r, s, e=0;
		long long result=1000000000000000000LL;
		
		cin >> n >> p >> q >> r >> s;
		for(int i=0;i<n;i++)
			supto[i+1] = supto[i] + (1LL * i * p + q) % r + s;
		
		for(int i=0;i<n;i++) {
			while(e < n && supto[n] - supto[e] > supto[e] - supto[i] ) {
				result = min(result, max(max(supto[i], supto[e] - supto[i]), supto[n] - supto[e]) );
				e++;
			}
			result = min(result, max(max(supto[i], supto[e] - supto[i]), supto[n] - supto[e]) );
		}
		
		cout << fixed << setprecision(10) << "Case #" << TCASE + 1 << ": " << 1.0 * (supto[n] - result) / supto[n] << '\n';
	}
	return 0;
}
