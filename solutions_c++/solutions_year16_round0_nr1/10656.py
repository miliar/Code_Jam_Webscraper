#include <iostream>
#include <map>
using namespace std;

int main() {

	int t;
	cin >> t;
	for(int z = 1; z <= t; z++) {
		int n;
		cin >> n;
		if(n == 0) {
			cout << "Case #" << z << ": INSOMNIA" << endl;
		} else {
			int val = n;
			map<int,int> mp;
			bool flag = 0;
			for(int i = 2; ; i++) {
				while(val != 0) {
					int digit = val % 10;
					val /= 10;
					mp[digit] = 1;
					if(mp.size() == 10) {
						flag = 1;
						break;
					}
				}
				if(flag == 1) {
					val = n * (i-1);
					break;
				}
				val = n * i;
			}
			cout << "Case #" << z << ": " << val << endl;
		}
	}
	return 0;
}
