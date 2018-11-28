#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <time.h>
using namespace std;

typedef pair<string,string> pss;

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);

	int t;
	scanf ("%d", &t);
	for (int it=1;it<=t;it++) {
		printf ("Case #%d: ", it);

		int n;
		pss arr[20];
		scanf ("%d", &n);

		for (int i=0;i<n;i++) {
			cin >> arr[i].first >> arr[i].second;
		}

		int mx = 0;
		for (int i=0;i<(1<<n);i++) {
			set <string> w1, w2;
			for (int j=0;j<n;j++) {
				if (i&(1<<j)) {
					w1.insert(arr[j].first);
					w2.insert(arr[j].second);
					//cout << arr[j].first << " " << arr[j].second << endl;
				}
			}
			int cur = 0;
			bool val = true;
			for (int j=0;j<n;j++) {
				if (i&(1<<j)) {
					continue;
				}
				cur ++;
				//cout << arr[j].first << " " << arr[j].second << endl;
				if (w1.find(arr[j].first) == w1.end() ||
						w2.find(arr[j].second)== w2.end()) {
					val = false;
				}
			}
			if (val) {
				mx = max (mx, cur);
			}
		}
		cout << mx << endl;
	}
	return 0;
}