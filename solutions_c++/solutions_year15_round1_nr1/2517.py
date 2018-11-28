#include<bits/stdc++.h>
using namespace std;
int t, n, ans1, temp, ans2, A[1015], curr, f;
int main()  {
	cin >> t;
	for(int kase = 1; kase <= t; kase++) {
		cin >> n;
		for(int i = 0; i < n; i++) {
			cin >> A[i];
		}
		ans1 = 0;
		temp = 0;
		ans2 = 0;
		f = 0;
		for(int i = 1; i < n; i++) {
			if(A[i] <= A[i - 1]) {
				ans1 += A[i - 1] - A[i];
			}
		}
		double rate = 0.0;
		curr = A[0];
		for(int i = 1; i < n; i++) {
			if(A[i] >= A[i - 1]) {
				rate = max(rate, 0.0); 
			} else {
				double r = ((A[i - 1] - A[i]) * (1.0)) / 10;
				rate = max(rate, r);
			}
		}
		//cout << rate << endl;
		for(int i = 0; i < n - 1; i++) {
			if(A[i] > rate * 10) {
				ans2 += rate * 10;
			} else {
				ans2 += A[i];
			}
		}
		cout << "Case #" << kase << ": " << ans1 << " " << ans2 << endl;
	}
}