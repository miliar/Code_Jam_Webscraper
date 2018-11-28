#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int t, n, x, s[10000];
	cin.sync_with_stdio(false);
	cin >> t;
	
	for(int TCASE = 0; TCASE < t; TCASE++) {
		cin >> n >> x;
		for(int i=0;i<n;i++)
			cin >> s[i];
		sort(s, s+n);
		
		int np=0, b=0, e = n-1;
		while(e > b) {
			while(e > 0 && s[b] + s[e] > x)
				e--;
			if(e > b)
				np++, e--;
			
			b++;
		}
		
		cout << "Case #" << TCASE+1 << ": " << n-np << '\n';
	}
	
	return 0;
}
