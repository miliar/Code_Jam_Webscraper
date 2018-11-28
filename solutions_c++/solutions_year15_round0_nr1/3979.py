#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
using namespace std;

int answer(int n, string a) {
	int count = 0;
	int additional = 0;
	for (int i = 0; i <= n; i++) {
		if (count < i) {
			int temp = i-count;
			count += temp;
			additional += temp;
		}
		count += (a[i]-'0');
	}
	return additional;
}

int main()
{
    int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		int n;
		string a;
		cin >> n >> a;
		printf("Case #%d: %d\n", _t, answer(n, a));
	}
    return 0;
}

