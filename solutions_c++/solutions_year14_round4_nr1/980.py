#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LL;

int main()
{
	freopen("E:\\Projects\\VS2010\\gcj2014\\gcj2014\\Round2\\A\\A--large.in", "r", stdin);
	freopen("E:\\Projects\\VS2010\\gcj2014\\gcj2014\\Round2\\A\\A.out", "w", stdout);
	int T;

	cin >>T;

	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		
		int n, x;

		cin >> n >> x;
		vector<int> s(n);

		

		vector<int> table(701, 0);

		for (int i=0; i<n; i++) {
			cin >> s[i];
			table[s[i]] ++;
		}

		sort (s.begin(), s.end());

		int result = 0;
		int nleft = n;
		for (int i=0; nleft && i<n; i++) {

			int target = s[i];
			if (table[target] == 0) {
				continue;
			}
			table[target]--;

			int start = x-target;

			for (int j=start; j>0; j--) {
				if (table[j]) {
					table[j] --;
					nleft -- ;
					break;
				}
				
			}
			nleft -- ;
			result ++;
		}
		cout << result << endl;
	}
	return 0;
}