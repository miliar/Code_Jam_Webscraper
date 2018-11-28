#include <iostream>
#include <cstring>
#define show(x) cerr << #x << '=' << x << endl;

using namespace std;

const int MAX = (1 << 16 ) + 10;

int main() {
	cout << "Case #1:" << endl;
	int J = 50;
	int counter = 0;
	for(int i=1; i< (1<<16); i++) {
		if (i % 2 == 0)
			continue;
		int a[100];
		int n =0;
		memset(a, 0, sizeof a);
		for(int j=0; j<16; j++)
			if (i & (1 << j)) {
				a[j] = 1;
				n = j + 1;
			}
		if (n != 16)
			continue;
		int keys[20];

		bool flag = 1;
		for (int base = 2; base <= 10; base++) {
			long long x = 0;
			long long b = 1;
			for(int j=0; j < n; j++) {
				x += a[j] * b;
				b *= base;
			}
			keys[base] = 0;
			for(long long i=2; i*i <= x; i++)
			{
				if (x % i == 0) {
					keys[base] = i;
					break;
				}
			}
			if (keys[base] == 0)  {
				flag = 0;
				break;
			}
		}
		if (flag) {
			counter ++;
			for(int j=n-1; j>=0; j--)
				cout << a[j];
			cout << " ";
			for(int base = 2; base <= 10; base ++)
				cout << keys[base] << " ";
			cout << endl;
		}
		if(counter == J)
			break;
	}
}
