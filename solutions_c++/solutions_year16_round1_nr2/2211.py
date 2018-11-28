#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int n;

int t;


int vis[3300];

int ans[100];

int tt;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B_output.txt", "w", stdout);
	cin >> t;
	int i,j,k;
	int a;
	for(i = 1; i <= t; i ++) {
		tt = 0;
		cin >> n;
		for(j = 0; j < 2 * n - 1; j++) {
			for(k = 0; k < n; k++) {
				cin >> a;
				vis[a]++;
			}
		}
		for(j = 0; j < 3000; j++) {
			if(vis[j] & 1) {
				ans[tt++] = j;
			}
		}

		cout << "Case #" << i << ": ";
		
		for(j = 0; j < tt; j++) {
			cout << ans[j] << " ";
		}
		cout << endl;
	}

	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
