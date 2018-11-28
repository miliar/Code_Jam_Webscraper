#include <iostream>
#include <math.h>


using namespace std;
char b1[100], b2[100];

int isPalin(long n) {
	long temp = n, reverse = 0;
 
	while( temp != 0 )
	{
		reverse = reverse * 10;
		reverse = reverse + temp%10;
		temp = temp/10;
	}
	return n == reverse;
}


int main() {
	int T;
	long long A, B;

	cin >> T;
	for (int p = 1; p <= T; p++) {
		cin >> A >> B;
		long long st, en;
		int cnt = 0;
		st = (long long)sqrt((double)A);
		en = (long long)sqrt((double)B);

		if(st*st < A)
			st++;

		for(long long i = st; i <=en; i++) {
			if(isPalin(i) && isPalin(i*i))
				cnt++;
		}

		cout << "Case #" << p << ": "<< cnt << endl;
	}
}