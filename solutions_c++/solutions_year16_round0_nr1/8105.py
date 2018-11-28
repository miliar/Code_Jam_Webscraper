#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
typedef long long ll;
typedef pair<int,int> pii;

int main() {
	int t, n;
	cin >> t;
	rep(tt, t) {
		int n;
		cin >> n;
		if(n == 0) {
			cout << "Case #" << (tt+1) << ": INSOMNIA" << endl;
			continue;
		}

		bool d[10] = {};
		int k = n;
		int cnt = 0;
		while(1) {
			int tmp = k;
			while(tmp>0) {
				int x = tmp%10;
				if(!d[x]) cnt++;
				d[x] = true;
				tmp /= 10;
			}
			if(cnt == 10) break;
			k += n;
		}
		cout << "Case #" << (tt+1) << ": " << k << endl;
	}
	return 0;
}
