#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#pragma warning(disable : 4996)

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	int N;
	int a[1003];
	int res1 = 0, res2 = 0;
	for(int i = 0; i < T; ++i) {
		res1 = 0;
		res2 = 0;
		cin >> N;
		for(int j = 0; j < N; ++j) 
			cin >> a[j];
		for(int k = 1; k < N; ++k) {
				if(a[k] < a[k-1])
					res1 += a[k-1] - a[k];
			}
		int tmp = 0;
		for(int k = 1; k < N; ++k) 
			if(a[k-1] > a[k])
				tmp = max(tmp, a[k-1]-a[k]);
		for(int l = 0; l < N-1; ++l)
			if(a[l] < tmp) res2 += a[l];
			else res2 += tmp;
		cout << "Case #" << i+1 << ": " << res1 << " " << res2 << "\n";
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}