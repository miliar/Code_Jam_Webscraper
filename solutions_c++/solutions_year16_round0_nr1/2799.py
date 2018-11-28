#include <iostream>
using namespace std;

int main() {
	int tc;
	cin >> tc;
	for(int z = 1; z <= tc; z++) {
		cout << "Case #" << z  << ": ";
		int n, mask = 0, found = 0;
		cin >> n;
		for(int i = 1; i <= 1000; i++) {
			int x = n * i;
			while(x) {
				mask |= 1 << (x%10);
				x /= 10;
			}
			if(mask == (1 << 10) - 1) {
				cout << n*i << endl;
				found = 1;
				break;
			}
		}
		if(!found)
			cout << "INSOMNIA" << endl;
	}
}
