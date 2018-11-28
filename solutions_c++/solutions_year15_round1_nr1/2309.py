#include <iostream>

using namespace std;
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	long t,n,i,k1,k2,d ;

	cin >> t;
	for (int cases = 0; cases < t; cases++){
		cin >> n;
		long *m = new long[n];
		k1 = 0;
		k2 = 0;
		d = 0;
		for (i = 0; i < n; i++) cin >> m[i];
		for (i = 1; i < n; i++) if (m[i - 1] > m[i]) k1 += ( -m[i]+m[i-1]);
		for (i = n - 1; i >= 1;i--) 
			if (m[i] < m[i - 1])
			{
				if (m[i-1]-m[i]>d)
				d = m[i - 1] - m[i];
				
			}
		if (d == 0) k2 = 0;
		else {
			for (i = 0; i < n - 1; i++)
				k2 += (m[i] < d) ? m[i] : d;
		}
		cout << "Case #" << cases + 1 << ": " <<k1<<" "<<k2<< endl;
		delete [] m;
	}
	
		return 0;
}