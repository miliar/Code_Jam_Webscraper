#include<iostream>

using namespace std;

int main() {
	int n;
	
	freopen("A-large.in", "r", stdin);
	freopen("output-large.txt", "w", stdout);
	
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		long long a;
		cin >> a;
		
		if(a == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		
		int digits[10];
		for(int j = 0 ; j < 10; j++) {
			digits[j] = 0;
		}
		
		bool finish = false;
		int coef = 1;
		while(!finish) {
			long long b = a * coef;
			while(b > 0) {
				digits[b % 10] = 1;
				int h = 0;
				for(int k = 0 ; k < 10; k++) {
					if(digits[k] == 1) {
						h++;
					}
				}
				if(h == 10) {
					finish = true;
				}
				b = b/10;
			}
			coef++;
		}
		coef--;
		cout << "Case #" << i << ": " << coef * a << endl;
	}
	
	
	
	
	return 0;
}