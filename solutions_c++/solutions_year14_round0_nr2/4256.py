#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
	if(fopen("cookie.in","r")) {
		freopen("cookie.in","r",stdin);
		freopen("cookie.out","w",stdout);
	}

	int t;
	cin >> t;
	double c, f, x;
	double secs;
	int numfarm = 0;
	for(int i = 1; i <= t; i++) {
		cout << "Case #";
		cout << i; 
		cout << ": ";
		secs = 0;

		cin >> c;
		cin >> f;
		cin >> x;
		cout << fixed << setprecision(7);
		if(c > x) {
			secs += x/2;
			cout << secs << '\n';
		}
		else{
			if((int) (f*x - 2*c - f*c) % (int) (f*c) == 0) {
				numfarm = (int) (f*x - 2*c - f*c)/(f*c);
			}
			else numfarm = (int) (f*x - 2*c - f*c)/(f*c) + 1;
			for(int j = 0; j <= numfarm; j++) {
				secs += (c)/(2 + f* (double) j);
			}
			secs += (x-c)/(2 + f* (double) numfarm);
			cout << secs << '\n';
		}
		
	}
	return 0;
}