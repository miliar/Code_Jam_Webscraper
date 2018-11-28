#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

long long int num;
int digit[500];
int N, J;

long long int checkPrime();
void buildNum(int base);
bool addOne();

int main(){
	int t, tCounter;
	cin >> t;
	int i, j, k;
	long long divisors[11];
	int base, count;
	int totalNumbers;
	for (tCounter = 1; tCounter <= t; tCounter++) {
		cin >> N >> J;
		cout << "Case #" << tCounter << ":" << endl;
		for (i = 0; i < N; i++)
			digit[i] = 0;
		digit[0] = digit[N - 1] = 1;
		totalNumbers = 0;
		while(totalNumbers < J) {
			count=0;
			for (base = 2; base <= 10; base++) {
				buildNum(base);
				divisors[base] = checkPrime();
				if (divisors[base] > 0)
					count++;
			}
			if (count == 9) {
				totalNumbers++;
				for (i = 0; i < N; i++)
					cout << digit[i];
				for (base = 2; base <= 10; base++)
					cout << " " << divisors[base];
				cout << endl;				
			}
			if (!addOne())
				break;
		}
	}
	return 0;
}

void buildNum(int base) {
	long long int basePowered=1;
	int i;
	num=0;
	for (i = N-1; i >=0; i--) {
		if (digit[i] == 1)
			num += + basePowered;
		basePowered *= base;
	}
	return;
}

bool addOne() {
	int carry=1;
	int index=N-2;
	while (carry && index>0) {
		digit[index] += carry;
		if (digit[index] > 1)
			digit[index] = 0;
		else
			carry = 0;
		index--;
	}
	if (index == 0)
		return false;
	return true;
}

long long int checkPrime() {
	long long myDivisor;
	bool found = false;
	long long max = sqrt(num);
	for (myDivisor = 2; !found && myDivisor <= max; myDivisor++)
		if (num % myDivisor == 0)
			found = true;
	myDivisor--;

	if (found)
		return myDivisor;
	return 0;
}

