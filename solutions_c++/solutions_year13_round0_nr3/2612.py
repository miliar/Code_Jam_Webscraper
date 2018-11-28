#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

bool pal(int x) {
	int a[32];
	int n = 0;

	do
	{
		a[n++] = x % 10;
		x /= 10;
	} while (x != 0);

	for (int i = 0, j = n - 1; i < j; ++i, --j)
		if (a[i] != a[j])
			return false;

	return true;
}

int main() {
	int T;

	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int A, B;

		cin >> A >> B;
		int count = 0; 

		int x = 1;
		while (x * x < A)
			++x;

		while (x * x <= B)
		{
			if (pal(x) && pal(x * x))
				++count;
			++x;
		}

		cout << "Case #" << t << ": " << count << endl;
	}

	return 0;
}

