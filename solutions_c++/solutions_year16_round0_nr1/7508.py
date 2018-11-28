#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	unsigned long long int t, n, m = 1, flag, p, i, c, x;
	cin >> t;
	while(t--) {
		cin >> n;
		flag = 0;
		c = 1;
		x = n;
		int a[10] = {0};
		cout << "Case #" << m << ": ";
		m++;
		if(n == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			while(flag == 0) {
				p = n;
				c++;
				flag = 1;
				while(p > 0) {
					a[p%10] = 1;
					p /= 10;
				}
				for(i=0; i<10; i++) {
					if(a[i] == 0) {
						flag = 0;
					}
					//cout << i << " : " << a[i] << endl;
				}
				if(flag == 0) {
					n = x*c;
				}
			}
			cout << n << endl;
		}
	}
	return 0;
}
