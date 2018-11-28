#include <iostream>

using namespace std;

int gcd(int m, int n)
{
        int temp = 0;
        if(m < n)
        {
                temp = m;
                m = n;
                n = temp;
        }
        while(n != 0)
        {
                temp = m % n;
                m = n;
                n = temp;
        }
        return m;
}
int min (int a, int b) {
	return a > b ? b : a;
}

int findGeneration (long long num, long long den) {
	if (num == 0) {
		return 0;
	}
	int k = 0, l = 0;
	while (den > 1) {
		if (den % 2 != 0) {
			return -1;
		}
		den /= 2;
		k ++;
	}
	while (num > 1) {
		num /= 2;
		l ++;
	}
	return k - l;
}

int main () {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int num, den;
		char c;
		cin >> num >> c >> den;
		int g = gcd (num, den);
		num /= g;
		den /= g;
		
		int ret = findGeneration (num, den);
		cout << "Case #" << (i + 1) << ": ";
		if (ret == -1) {
			cout << "impossible" << endl;
		} else {
			cout << ret << endl;
		}
	}
	return 0;
}

