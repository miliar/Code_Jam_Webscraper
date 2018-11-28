#include <iostream>

using namespace std;

int main(void)
{
	int t,n,k;
	int flg;
	cin >> t;
	for(int i=1;i<=t; i++) {
		flg = 0;
                k = 1;
		cout << "Case #" << i << ": ";
		cin >> n;
		if(n==0) {
			cout << "INSOMNIA" << endl;
		}
                else {
			while(flg < 1023) {
				int c = k*n;
//cout << c << endl;
				do {
					int ld = c%10;
					flg |= (1 << ld);
//cout << flg << endl;
					c /=10;
				} while(c);
				k++;
                        }
			cout << (k-1)*n << endl;
                }
	}
}
