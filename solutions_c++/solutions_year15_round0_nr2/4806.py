#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxn = 1001;

int T, t;
int n, s;
int d[maxn] = {0};

int main() {
	
	cin >> T;
	
	for (t = 0; t < T; t ++) {
		cin >> n;
		memset(d,0,sizeof(d));
		int maxs = -1;
		for (int i = 0; i < n ; i ++) {
			cin >> s;
			d[s] ++;
			maxs = max(s,maxs);
		}
		
		int ans = 1001;
		if (maxs == 0)
			ans = 0;
		for (int i = maxs; i >= 1; i --) {
			int r = 0;
			for(int j = maxs; j > i ; j --) {
				r += (j/i - (j % i == 0)) * d[j];
			}
			r += i;
			//cout << i << ' ' << r << endl;
			if (r < ans)
				ans = r;
		} 
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	// your code goes here
	return 0;
}