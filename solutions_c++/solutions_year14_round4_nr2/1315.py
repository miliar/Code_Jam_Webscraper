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
long long A[1024];

struct BIT {
	long long data[2048];
	void update(int idx, long long val){
		idx = n - idx;
		while (idx < 2048) {
			data[idx] += val;
			idx += idx & (-idx);
		}
	}
	long long query(int idx) {
		idx = n - idx;
		long long ret = 0;
		while (idx > 0) {
			ret += data[idx];
			idx -= idx & (-idx);
		}
		return ret;
	}
} bit;

long long x[1024];
long long y[1024];
pair<long long, long long> x2[1024];

long long inversions2() {
	for (int i = 0; i < n; i ++) {
		x2[i].first = x[i];
		x2[i].second = i;
	}
	sort(x2, x2 + n);
	
	long long ret = 0;
	for (int i = 0; i < n; i ++) {
		ret += bit.query(x2[i].second);
		bit.update(x2[i].second, 1);
	}
	return ret;
}

long long inversions() {
	long long ret = 0;
	for (int i = 0; i <n; i ++)
		for (int j = 0; j < i; j ++)
			if (x[j] > x[i])
				ret ++;
	return ret;			
}

int n2;

bool valid() {
	int ak = 0;
	int ak2 = 0;
	for (int i = 1; i < n2-1; i ++) {
		if (y[i] > y[i-1] and y[i] > y[i+1])
			ak ++;
		if (y[i] < y[i-1] and y[i] < y[i+1])
			ak2 ++;
	}
	return ak <= 1 and ak2 == 0;
}

int main () {
	cin >> t;
	int caze = 0;
	
	while (t --) {
		caze ++;
		cin >> n2;
		for (int i = 0; i < n2; i ++)
			cin >> A[i];

		long long ans = 1000000000;
	
		n = n2;
		for (int i = 0 ; i < n2; i ++)
			x[i] = i;
			
		do {
			for (int i = 0 ; i < n2; i ++)
				y[i] = A[x[i]];
			if (valid()) {
				memset(bit.data, 0, sizeof (bit.data));
				ans = min(ans, inversions());
			}
			
		} while(next_permutation(x, x+n2));
		
		
		cout << "Case #" << caze << ": " << ans << endl;
	}
	
	return 0;
}  	
