#include<iostream>
#include<cstring>
using namespace std;
int t, n, c, m;
bool f[10];
void split(int m) {
	while(m) {
		int d = m % 10;
		if(!f[d]) {
			f[d] = true;
			c++;
		}
		m /= 10;
	}
}
int main()
{
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> n;
		if(n == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		c = 0;
		memset(f, false, sizeof(f));
		int m = 0;
		for(int k = 1; k <= 100; k++) {
			m += n;
			split(m);
			if(c == 10) {
				cout << "Case #" << i << ": " << m << endl;
				break;
			}
		}
	}
	return 0;
}
			
			
