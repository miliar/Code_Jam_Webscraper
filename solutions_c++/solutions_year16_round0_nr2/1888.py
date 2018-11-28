#include <iostream>
#include <cstdio>

using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("/Users/malzantot/Documents/codingspace/B-large.in.txt", "r", stdin);
	freopen("/Users/malzantot/Documents/codingspace/B-large-out.txt", "w", stdout);

#endif

	int tt;
	cin >> tt;

	for (int ii = 1; ii <= tt; ii++) {
		string line;
		cin >> line;

		int cnt = 0;

		int flag = 0;
		for (int i = line.size()-1; i >= 0; i--) {
			if (flag==0 && line[i] == '-') {
				flag = 1;
				cnt ++;
			} else if (flag==1 && line[i] =='+') {
				flag=0;
				cnt++;
			} else {
				// continue
			}
		}
		printf("Case #%d: %d\n", ii, cnt);
	}
	
	return 0;

}
