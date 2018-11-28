#include<iostream>
#include<cstdlib>

using namespace std;

int main() {
	int t;
	int a[6];
	a[0] = 484;
	a[1] = 121;
	a[2] = 1;
	a[3] = 4;
	a[5] = 9;
	cin >> t;
	int m;
	int n;
	int k = 1;
	int count = 0;
	while(t--) {
		count = 0;
		cin >> m >> n;
		for(int i = 0 ; i < 6; i++) {
			if(m <= a[i] && a[i] <= n){
				count++;
			} 
		}
		cout << "Case #" << k << ": " << count << endl;
		k++;
	}
}