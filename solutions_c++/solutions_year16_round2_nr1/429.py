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

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);

	int t;
	scanf ("%d", &t);
	char x[2020];

	for (int it=1;it<=t;it++) {
		scanf ("%s", x);
		int n = strlen (x);
		map <char, int> mp;
		mp.clear();
		for (int i=0;i<n;i++) {
			if (mp.find(x[i]) == mp.end()) {
				mp[x[i]] = 0;
			}
			mp[x[i]]++;
		}

		int cnt[10];
		memset(cnt, 0, sizeof(cnt));
		string arr[] = {
			"EIGHT", "SIX", "FOUR", "FIVE", "SEVEN", "ZERO", "NINE", "ONE", "TWO", "THREE"
		};
		char key[] = "GXUFVZINWT";
		int val[] = {8, 6, 4, 5, 7, 0, 9, 1, 2, 3};

		for (int i=0;i<10;i++) {
			int k = mp[key[i]];
			for (int j=0;j<arr[i].size();j++) {
				mp[arr[i][j]] -= k;
			}
			cnt[val[i]] += k;
		}

		printf ("Case #%d: ", it);
		for (int i=0;i<10;i++) {
			for (int j=0;j<cnt[i];j++) {
				printf ("%d", i);
			}
		}
		printf ("\n");


	}

	return 0;
}