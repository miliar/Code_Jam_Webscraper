#include<bits/stdc++.h>
using namespace std;
priority_queue <int> C;
int A[1005];

int main() {
	int t, n, x;
	cin >> t;
	for(int kase = 1; kase <= t; kase++) {
		cin >> n;
		int temp = -1, temp1 = 0, ans = 1000000000;
		for(int i = 0; i < n; i++) {
			cin >> A[i];
			temp = max(temp, A[i]);
		}
		for(int i = temp; i >= 1; i--) {
			temp1 = 0;
			for(int j = 0; j < n; j++) {
				if(A[j] > i) {
					temp1 += (ceil((A[j]*1.0) / i)) - 1;
				}
			}
			temp1 += i;
			ans = min(ans, temp1);
		}
		cout << "Case #" << kase <<": " << ans << endl;
	}
}