#include <iostream>
#include <bitset>
using namespace std;

long countDigits(long k)

{
	int dig = 0;
	int d = 0;
	while (k != 0){
		d = k % 10;
		dig |= (1 << d);
		k /= 10;
	}
	return dig;
}

int main()
{
	const int ALL_ONES = (1 << 10)-1;
	int test = 0;
	cin >> test;
	for (int t = 1; t <= test; ++t){
		long digits = 0;
		long n = 0;
		cin >> n;
		if (n == 0)
			cout << "Case #" << t << ": INSOMNIA\n";
		else{
			int i = 2;
			long p = n;
			digits = countDigits(p);
			while (digits != ALL_ONES){
				p = n*i;
				++i;
				digits |= countDigits(p);
			}
			cout << "Case #" << t << ": " << p << endl;
		}
	}

	return 0;
}
