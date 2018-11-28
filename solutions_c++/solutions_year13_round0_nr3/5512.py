#include <iostream>
#include <cmath>
using namespace std;

int t, a, b;


bool ispal(int a) {
	int h[100];
	int l = 0;
	while (a) {
		h[l++] = a%10;
		a /= 10;
	}
	
	for (int i = 0; i < l; i++) {
		if (h[i] != h[l-1-i])
			return 0;
	}
	return 1;
}

int main() {
	cin >> t;

	//cout << ispal(111) << ispal(121) << ispal(123) << endl;
	//return 0;
	for (int i = 1; i <= t; i++) {
		cin >> a >> b;
		int cnt = 0;
		for (int x = a; x <= b; x++)
			if (ispal(x))
				if (ceil(sqrt(x)) == sqrt(x))
					if (ispal(sqrt(x)))
						cnt++;
		
		cout << "Case #" << i << ": " << cnt << endl;
		
	}
}
