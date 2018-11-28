#include <stdio.h>
#include <vector>

using namespace std;

#define pb push_back
#define mp make_pair
#define ff first
#define ss second

const int N = 1000 + 239;
const int inf = 100500;


vector < int > mrg(vector < int > &a, vector < int > &b) {
	vector < int > res (N, inf);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (i + j >= N)
				break;
			res[i + j] = min(res[i + j], max(a[i], b[j]));

		}
	}
	return res;
} 

int t, n;
int arr[N];

vector < int > calc(int l, int r) {
	vector < int > res(N, inf); 	
	if (l == r) {
	    for (int i = 0; i < N; ++i) 
	    	res[i] = (arr[l] - 1) / (i + 1) + 1;
	    return res;
	}
	int m = (l + r) / 2;
	vector < int > a = calc(l, m);
	vector < int > b = calc(m + 1, r);
	return mrg(a, b); 
}

int main() {
	scanf("%d", &t);
	for (int q = 0; q < t; ++q) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) 
			scanf("%d", &arr[i]);
		vector < int > res = calc(0, n - 1);
		int ans = inf;
		for (int i = 0; i < N; ++i) {
			ans = min(ans, i + res[i]);
		} 

		printf("Case #%d: %d\n", q + 1, ans);
	}

	return 0;
}
