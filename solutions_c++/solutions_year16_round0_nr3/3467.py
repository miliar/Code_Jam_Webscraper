#include <bits/stdc++.h>
using namespace std;
string digits = "1111111111111111";
//string digits = "11111111111111111111111111111111";
long long sieve[]= {2LL,3LL,5LL,7LL,11LL,13LL,17LL,19LL,23LL,29LL,31LL,37LL,41LL,43LL,47LL,53LL,59LL,61LL,67LL,71LL,73LL,79LL,83LL,89LL,97LL,101LL,103LL,107LL,109LL,113LL,127LL,131LL,137LL,139LL,149LL,151LL,157LL,163LL,167LL,173LL,179LL,181LL,191LL,193LL,197LL,199LL,211LL,223LL,227LL,229LL,233LL,239LL,241LL,251LL,257LL,263LL,269LL,271LL,277LL,281LL,283LL,293LL,307LL,311LL,313LL,317LL,331LL,337LL,347LL,349LL,353LL,359LL,367LL,373LL,379LL,383LL,389LL,397LL,401LL,409LL,419LL,421LL,431LL,433LL,439LL,443LL,449LL,457LL,461LL,463LL,467LL,479LL,487LL,491LL,499LL};
void permute() {
//	cout << digits <<endl;
	for (int i = 14; i > 0; i--) {
		if (digits[i] == '0') {
			digits[i] = '1';
			for (int j = i+1; j <= 14; j++) {
				digits[j] = '0';
			}
			return;
		}
		
	}
}

int main() {
	
//	freopen ("A-large-out.txt","w",stdout);

	cout << "Case #1:\n";

	digits[0] = '1';
	digits[15] = '1';
	for (int i = 1; i < 15; i++) {
		digits[i] = '0';
	}
	int counter = 0;
	while (counter < 50) {
		permute();
		string x = digits;
	//	cout << x << endl;
		bool fail = false;
		long long arr[15] = {0};

		for (int i = 2; i <= 10; i++) {
			long long t = stoll(x, 0, i);
			bool composite = false;
			
			for (int j = 0; j < 95; j++) {
				if (t % sieve[j] == 0) {
					//Pass
					composite = true;
					arr[i] = sieve[j];
					break;
				}
			}
			if (!composite) { fail = true; break; }
		}
		if (!fail) {
			counter++;
			cout << x;
			for (int i = 2; i <= 10; i++) {
				printf(" %lld", arr[i]);
			}
			printf("\n");
		}

	}

	
	return 0;
}
