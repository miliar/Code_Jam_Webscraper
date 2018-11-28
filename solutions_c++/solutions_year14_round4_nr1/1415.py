#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#define print(Z,a,b) for (int __z = a; __z < b; __z ++) cout << Z[__z] << " ";
#define scan(Z,a,b) for (int __z = a; __z < b; __z ++) cin >> Z[__z];
#define bit(_z) (1ll << _z)
using namespace std;

int t;
int n;
int A[12435], X;

int main () {
	cin >> t;
	int caze = 0;
	
	while (t --) {
		caze ++;
		cin >> n >> X;
		scan(A, 0, n);
		
		sort(A, A + n);
		
		int l = 0, r = n-1;
		int ans = 0;
		while (l < r) {
			if (A[l] + A[r] <= X) {
				l ++;
				r --;
			}else {
				r --;
			}
			ans ++;
		}
		if (l == r)
			ans ++;
		
		cout << "Case #" << caze << ": " << ans << endl;
	}
	
	return 0;
}  	
