#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
	double sticks[2][1000];
	int T;
	cin >> T;
	for(int c=1;c<=T;c++) {
		int n;
		cin >> n;
		for(int i=0;i<n;i++) {
			cin >> sticks[0][i];
		}
		for(int i=0;i<n;i++) {
			cin >> sticks[1][i];
		}
		sort(sticks[0],sticks[0]+n);
		sort(sticks[1],sticks[1]+n);
		cout << "Case #" << c << ": ";
		int pts = 0;
		int index = n-1;
		for(int i=n-1;i>=0;i--) {
			while(index >= 0) {
				if(sticks[0][index] < sticks[1][i]) {
					pts++;
					index--;
					break;
				} else {
					index--;
				}
			}
		}
		int ans = 0;
		index = 0;
		for(int i=0;i<n;i++) {
			if(sticks[0][i] > sticks[1][index]) {
				ans++;
				index++;
			}
		}
		cout << ans << " " << n-pts << endl;
	}
	return 0;
}