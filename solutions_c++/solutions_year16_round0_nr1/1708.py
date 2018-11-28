#include <iostream>

using namespace std;

#define ULL unsigned long long

int main() {
	ios_base::sync_with_stdio(0);
	ULL t;
	cin >> t;
	
	for (ULL T = 1; T <= t; T++) {
		ULL n;
		cin >> n;
		
		if (n == 0) {
			cout << "Case #" << T << ": INSOMNIA\n";
			continue;
		}
		
		bool digits[10] = {false};
		ULL howMany = 0;
		ULL tmp = 0;
		
		while (howMany != 10) {
			tmp += n;
			ULL tmp2 = tmp;
			
			while (tmp2 != 0) {
				if (!digits[tmp2 % 10]) {
					digits[tmp2 % 10] = true;
					howMany++;
				}
				
				tmp2 /= 10;
			}
		}
		
		cout << "Case #" << T << ": " << tmp << "\n";
	}
	
	return 0;
}
