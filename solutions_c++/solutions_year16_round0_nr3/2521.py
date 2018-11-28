#include <iostream>
#include <cstring>
using namespace std;
#define UL unsigned long
#define ULL unsigned long long

UL p[6543] = {2,3,0};
UL 	MAX_P = 65535, 
	pc = 2;

void generatePrimes() {
	UL m, tp;
	for (UL n = 5; n <= MAX_P; n++) {
		bool isPrime = true;

		m = n / 2 + 1;
		for (UL i = 0; i < pc && (tp = p[i], tp <= m); i++) {
			if (n % tp == 0) {
				isPrime = false;
				break;
			}
		}

		if (isPrime) {
			p[pc++] = n;

		}
	}
}

char *getBase2String(UL dec, char str[65]) {
	int b = 2;
	if (dec == 0) {
		// cout<<"0";
		return 0;
	}
	else {
		int i = 0;
		while(dec) {
			str[i] = '0' + (dec % b);
			dec /= b;
			i++;
		}
		str[i] = 0;
		strrev(str);
		return str;
	}
}

ULL getNum(char *str, UL b) {
	int i = 0;
	ULL d = 0;
	ULL f = 1;
	strrev(str);
	while(str[i]) {
		d += (str[i]-'0') * f;
		f *= b;
		i++;
	}
	strrev(str);
	return d;
}


ULL getNum1(ULL dec, UL b) {
	char str[65];
	char s1[65];
	if (dec == 0) {
		// cout<<"0";
		return 0;
	}
	else {
		int i = 0;
		while(dec) {
			str[i] = '0' + (dec % b);
			dec /= b;
			i++;
		}
		str[i] = 0;
strrev(str);
ULL d;
sscanf(str,"%ull",&d);
// cout<<d;
return d;
		// while(i--) {
		// 	cout<<str[i];

		// }

	}
}

bool isNumPrime(ULL o, ULL &tp) {
	// cout<<"["<<o<<"]";
	bool isPrime = true;
	ULL m = o / 2 + 1;
	for (UL i = 0; i < pc && (tp = p[i], tp < m); i++) {
		if (o % tp == 0) {
			isPrime = false;
			break;
		}
	}

	return isPrime;
}

int main() {
	generatePrimes();

	UL T, n,j, o, d1,d2;
	ULL tp;
	cin>>T;
	char str[65];
	ULL nums[12];

	for (UL ti = 1; ti <= T; ti++) {
		cout<<"Case #"<<ti<<": "<<endl;
		cin>>n>>j;
		d1 = (1UL<<(n-1))+1;
		if (d1 % 2 == 0) d2++;
		d2 = ~((~1UL)<<(n-1));

		for (UL o = d1, jc = 0; jc < j && o <= d2; o+=2) {
			getBase2String(o,str);
			bool isPrime = false;
			ULL num;
			for (UL b = 2; b <= 10; b++) {
				num = getNum(str, b);
				// cout<<"["<<num<<"] ";
				if ( isNumPrime(num, tp) ) {
					isPrime = true;
					break;
				}
				nums[b] = tp;
			}

			if (!isPrime) {
				cout<<str<<" ";
				for (UL b = 2; b < 10; b++) {
					cout<<nums[b]<<" ";
				}
				cout<<nums[10];
				jc++;
				cout<<endl;
			}
		}
	}

	return 0;
}