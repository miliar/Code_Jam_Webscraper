#include <iostream>

using namespace std;

int main()
{
	unsigned long long int a, b, c, n, t, i, j, flag;
	cin >> t;

	for (i = 0; i < t; ++i) {
		int arr[10];
		for (j = 0; j < 10; ++j) {
			arr[j] = 0;
		}

		cin >> n;
		a = n;
		flag = 0;
		while (1) {
			b = a;
			while (a) {
				arr[a%10]++;
				a /= 10;
			}
			flag = 1; 
			for (j = 0; j < 10; ++j) {
				if (arr[j] == 0) flag = 0;	
			}
			if (flag == 1) {
				break;
			}
			a = b + n;
			if (a == b) {
				cout << "Case #"<< i+1 << ": INSOMNIA" << endl;
				break;
			}
		}
		if (flag == 1) {
			cout << "Case #" << i+1 << ": " << b << endl;
		}
	}

	return 0;
}
