#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
	freopen("bullseye.out", "w", stdout);
	freopen("bullseye.in", "r", stdin);
	
	long long T, r, t;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> r >> t;
		long long num = 0, cur = r+1;
		while (t >= 0) {
			t -= cur*cur-(cur-1)*(cur-1);
			cur += 2;
			num++;
		}
		num--;
		cout << "Case #" << (i+1) << ": " << num << endl;
	}
	return 0;
}		
