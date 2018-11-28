#include<bits/stdc++.h>
using namespace std;

int main() {
	long long total,r,t,n,answer;
	string s;
	cin >> n;
	for(long long i = 1 ; i <= n ; i++) {
		cin >> t;
		cin >> s;
		total = answer = 0;
		for(long long j = 0; j <= t;j++) {
			r = int(s[j] - '0');
			if(total < j) {
				answer += j-total;
				total = j;
			}
			total += r;
		}
		cout << "Case #" << i << ": " << answer << endl;
	}
	return 0;
}