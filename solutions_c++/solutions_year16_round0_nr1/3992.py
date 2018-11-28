#include <bits/stdc++.h>
using namespace std;
int digits[15];
void split(int n) {
	while (n != 0) {
		int temp = n % 10;
		digits[temp] = 1;
		n /= 10;
	}
}

int main() {

	freopen ("A-large.in","r",stdin);
	freopen ("A-large-out.txt","w",stdout);


	int tc;
	cin >> tc;
	for (int i = 1; i <= tc; i++) {
		int n;
		
		for (int j = 0; j < 15; j++) {
			digits[j] = 0;
		}
		cin >> n;
		bool flag= false;
		for (int j = 1; j <= 200; j++) {
			split(n*j);
			bool fail = false;
			for (int k = 0; k < 10; k++) {
				if (digits[k] == 0) {
					fail = true;
				}
			}
			
			
			if (fail) continue;
			else {
				printf("Case #%d: %d\n", i, n*j);
				flag = true;
				break;
			}
		}
		if (flag == false) printf("Case #%d: INSOMNIA\n", i);
	}
	// your code goes here
	return 0;
}
