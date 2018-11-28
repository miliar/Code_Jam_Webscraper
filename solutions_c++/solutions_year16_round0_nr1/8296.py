
#include <iostream>
using namespace std;



int main()
{
	int t;
	cin >> t;

	for (int X = 1; X <= t; X++) {
		int n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << X << ": INSOMNIA" <<  endl;
			continue;
		}
		int a[10] = { 1,1,1,1,1,1,1,1,1,1 };
		int cnt = 10;
		int tn = 0;
		while (cnt) {
			tn += n;
			int tz = tn;
			while (tz) {
				int nd = tz % 10;
				if (a[nd]) {
					a[nd] = 0;
					cnt--;
				}
				tz /= 10;
			}
		}
		cout << "Case #" << X << ": " << tn << endl;
	}
    return 0;
}


