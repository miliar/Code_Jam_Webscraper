#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

void solvePr4() {
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		int n;
		cin >> n;
		vector <double> arr1(n);
		vector <double> arr2(n);
		FOR(i,0,n) {
			cin >> arr1[i];
		}
		FOR(i,0,n) {
			cin >> arr2[i];
		}
		sort(arr1.begin(), arr1.end());
		sort(arr2.begin(), arr2.end());
		int ans2 = n;
		vector <bool> flag(n, false);
		FORI(i,n,0) {
			FOR(j,0,n) {
				if(!flag[j] && arr1[i] <= arr2[j]) {
					ans2--;
					flag[j] = true;
					break;
				}
			}
		}
		int i1 = 0;
		int j = n - 1;
		int ans1 = n;
		FORI(i,n,i1) {
			if(j < 0) {
				break;
			}
			if(arr1[i] <= arr2[j]) {
				i1++;
				i++;
				ans1--;
			}
			j--;
		}
		cout << "Case #" << tc << ": " << ans1 << " " << ans2 << endl;
	}
}

int main() {
	freopen("C:/Users/deepd/Downloads/in.txt", "r", stdin);
	freopen("C:/Users/deepd/Downloads/out.txt", "w", stdout);
	solvePr4();
	return 0;
}
