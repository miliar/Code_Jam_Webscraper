#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int t, tCounter, k, c, s;
	cin >> t;
	int i, j;
	long long int index;
	int step;
	bool flag;
	for (tCounter = 1; tCounter <= t; tCounter++) {
		cin >> k >> c >> s;
		cout << "Case #" << tCounter << ": " ;
/*
// code for small set starts
		for (step = 0; step < k; step++) {
			index=step;
			for (i = 1; i < c; i++) {
				index = index * k + step;
			}
			cout << index + 1 << " ";
		}
// code for small set ends
*/
// code for large set starts
		if (k > s * c) 
			cout << "IMPOSSIBLE";
		else {
			step=0;
			flag=true;
			while (flag) {
				index = step;

				step++;
				if (step >= k)
					flag=false;
				
				for (i = 1; i < c; i++) {
					if (flag)
						index = index * k + step;
					
					step++;
					if (step >= k)
						flag=false;
				}
				cout << index + 1 << " ";
			}
		}
// code for large set ends
		cout << endl;
	}
	return 0;
}

