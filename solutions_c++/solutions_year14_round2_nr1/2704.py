#include <iostream>
#include <string>
#include <stdlib.h>     /* abs */
#include <math.h>       /* round, floor, ceil, trunc */

using namespace std;

int main()
{
	int i, j, l, n, m, k, c[110], d[110], a[110], b[110][110], t, o, z; 
	long double sm;
	long long av, tot;
	
	string s;
	
	cin >> o;
	for (t=0; t<o; t++) {
		z=0;
		cin >> n;
		cin >> s;
		for (j=0; j<105; j++) c[j]=0;
		for (j=0; j<105; j++) d[j]=0;
		j=0;
		k=0;
		l=0;
		while (j<s.size()) {
			if (int(s[j])==l) d[k]++;
			else {
				k++;
				c[k]=int(s[j]);
				l=c[k];
				d[k]=1;
			}
			j++;
		}
		m=k;
//		cout << m << endl;
		
		for (j=0; j<=m; j++) b[0][j]=d[j];
		
		for (i=1; i<n; i++) {
			cin >> s;
			for (j=0; j<105; j++) a[j]=0;
			for (j=0; j<105; j++) b[i][j]=0;
			j=0;
			k=0;
			l=0;
			while (j<s.size()) {
				if (int(s[j])==l) b[i][k]++;
				else {
					k++;
					a[k]=int(s[j]);
					l=a[k];
					b[i][k]=1;
				}
				j++;
			}
			for (j=0; j<=m+2; j++) 
				if (a[j]!=c[j]) z++;
		}
	
		if (z) cout << "Case #" << t+1 << ": Fegla Won" << endl;
		else {
			tot=0;
			for (j=1; j<=m; j++) {
				sm=0.0;
				for (i=0; i<n; i++) 
					sm+=b[i][j];
				av=round(sm/n);
				//cout << av << endl;
				for (i=0; i<n; i++) {
					tot+=abs(av-b[i][j]);
				//	cout << b[i][j];
				}
			//	cout << endl;
			}
			cout << "Case #" << t+1 << ": " << tot << endl;
		}
	}
	return 0;
}
