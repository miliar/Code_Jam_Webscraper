#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		int n;
		cin >> n;
		vector <int> arr(n);
		for(int i = 0 ; i < n ; i++) {
			cin >> arr[i];
		}
		int maxdiff = 0;
		for(int i = 0 ; i < n - 1 ; i++) {
			maxdiff = max(maxdiff, arr[i] - arr[i+1]);
		}
		int c1 = 0;
		int c2 = 0;
		for(int i = 0 ; i < n - 1 ; i++) {
			if(arr[i+1] < arr[i]) {
				c1 = c1 + arr[i] - arr[i+1];
			}
		}
		for(int i = 0 ; i < n - 1 ; i++) {
			c2 = c2 + min(arr[i], maxdiff);
		}
		cout << "Case #" << tc << ": " << c1 << " " << c2 << endl;
	}
	return 0;
}
