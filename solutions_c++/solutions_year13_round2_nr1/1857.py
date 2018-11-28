#include <iostream>
#include <algorithm>
using namespace std;

long long int a[2000005];

int main()
{
	long long int t, n, k, i, j, u = 1;
	cin >> t;
	while (t--) {
		cin >> k >> n;
		for (i = 0; i < n; i++) {
			cin >> a[i];
		}
		sort(a, a + n);

		long long int mini = n;
		i = 0;
		long long int sm = k;
		long long int x = 0;   //insertions
		
		while (i < n) {
			if (i < n && a[i] < sm) {
				sm += a[i];
				i++;
			} else if (i == n) {
				mini = min(mini, n - i + x);
	//			cout << mini << ".." << endl;
				break;
			} else {
				mini = min(mini, n - i + x);
	//			cout << mini << "..." << endl;
				x++;
				//if ((sm - 1) * ((1<<(n - i)) - 1) < a[i]) {
				//if (sm == 1) {
				//if ((n - i) * (sm - 1))
				if (sm == 1) {
					mini = min(mini, n - i + x);
	//				cout << "i = " << i << " x  =  " << x << endl;
	//				cout << mini << "....." << endl;
					break;
				}
				sm += sm - 1;
			}
		}
	//	if (a[i] < sm) {
//		cout << "i = " << i << " x  =  " << x << endl;
		mini = min (mini, n - i + x);
	//	} else {
//		if ()
		cout << "Case #" << u++ << ": " << mini << endl;
		//}
	}
	return 0;
}
		/*
		while (i < n) {
			//cout << "hi" << endl;
			while (i + 1 < n && a[i] + sm < a[i + 1]) {
				sm += a[i];
				//cout << "hei";
				i++;
			}
			if (i + 1 >= n) {
				mini = min(x, mini);
				cout << mini << "..." << endl;
				break;
			}  else if (a[i] + sm >= a[i + 1]) {
				mini = min(mini, n - i + x);
				cout << mini << "....." << endl;
				x += 1;
				sm = 2 * sm - 1 + a[i];
				i++;

				//cout << "hel" << endl;
			}
		}
		if (sm < a[i + 1]) {

		mini = min(mini, n - i + x);

		cout << "Case #" << u++ << ": " << mini << endl;
	}
	return 0;
}

		i = 0;
		int sm = 0;
		while (i + 1 < n && a[i] + sm < a[i + 1]) {
			sm += a[i];
		}
		if (i + 1 == n) {
			cout << "Case #" << u++ << ": " << 0 << endl;
		} else {
			int x = 0;
			int mini = n - i;
			while (i < n) {
				sm += n - 1;
				x = 1;
				while (i + 1 < n && a[i] + sm < a[i + 1]) {
					sm += a[i];
				}
				if (i + 1 )
				x += n - i;
				mini = 		}
	}
	return 0;
}*/
