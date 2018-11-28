#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

double a[1100], b[1100];

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++){
		int resulta = 0, resultb = 0;
		int n;
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> a[i];
		}
		for(int i = 0; i < n; i++){
			cin >> b[i];
		}

		sort(a, a + n);
		sort(b, b + n);

		int ap = 0, bp = 0;
		while(ap < n){
			while(a[ap] < b[bp] && ap < n){
				ap++;
			}
			if (ap < n){
				if (a[ap] > b[bp]){
					resulta++;
					bp++;
					ap++;
				}
			}
		}

		ap = 0, bp =0;
		while(bp < n){
			while(b[bp] < a[ap] && bp < n){
				bp++;
			}
			if (bp < n){
				if (b[bp] > a[ap]){
					resultb++;
					bp++;
					ap++;
				}
			}
		}

		resultb = n - resultb;

		cout << "Case #" << tt << ": " << resulta << " " << resultb << endl;
	}
	return 0;
}