#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
using namespace std;

int answer(int r, int c, int w) {
	int count = c/w;
	if (c % w) count += w;
	else count += w-1;
	return count * r;
}

int main()
{
    int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		int r, c, w;
		cin >> r >> c >> w;
		cout << "Case #" << _t << ": " << answer(r, c, w) << endl;
	}
    return 0;
}
