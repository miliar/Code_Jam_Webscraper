#include <iostream>
#include <cmath>
using namespace std;


int primalityTest(long int n) {
	if (n % 2 == 0) return 2;
	long long max = floor(sqrt(n));

	for (long long i = 1; i < max; i++) {
		if (n % ((2 * i) + 1) == 0) return 2*i+1;
	}
	return -1;
}

long long expo(int base, int exp) {
	if(exp==0)
		return 1;

	long long n = base;
	exp--;
	while(exp--)
		n *= base;

	return n;
}

long long getBase(long long num, int base) {
	int pos=0;

	long long n = 0;

	while(num!=0) {
		if(num%10!=0)
			n += expo(base, pos);
		//cout << expo(base, pos) << endl;
		num/=10;
		pos++;
	}

	return n;
}



int main() {
	int cases;
	cin >> cases;

	long long n, j;

	cin >> n >> j;
	cout << "Case #1:" << endl;

	int found=0;

	long long num = (1<<(n-1));
	num += 1;

	while(found<j) {
	if(!(num&1)) {
		num++;
		continue;
	}
	long long test=0;
	string teststr = "";
	for(int i = n-1; i>=0; i--) {
		if(num&(1<<i)) {
			test += expo(10, i);
			teststr = teststr + "1";

		}
		else {
			teststr = teststr + "0";
		}

	}
	
	

	bool works=true;



	for(int i=1; i<10; i++)
		if(primalityTest(getBase(test, i+1))==-1)
			works = false;

	if(works) {
		cout << teststr << " ";
		for(int i=1; i<10; i++)
			cout << primalityTest(getBase(test, i+1)) << " ";
		found++;
		cout << endl;

	}

	num++;
		
	}
	return 0;
}