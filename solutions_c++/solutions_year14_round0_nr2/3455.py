#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <string.h>
#include <utility>
#include <vector>
using namespace std;
#define exp 1e-9

FILE *file;

int main() {
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\input.txt", "r", stdin);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\output.txt", "w", stdout);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\B-small-attempt0.in", "r", stdin);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\Small-output.out", "w", stdout);
	freopen_s(&file, "C:\\Users\\wayne\\Downloads\\B-large.in", "r", stdin);
	freopen_s(&file, "C:\\Users\\wayne\\Downloads\\Large-output.out", "w", stdout);
	int t;
	double c, f, x, buy, notbuy, produce, time;

	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> c >> f >> x;
		buy = notbuy = 0;
		produce = 2;
		while (true) {
			notbuy += x / produce;
			buy += c / produce;
			time = x / (produce + f);
			produce += f;
			if (buy + time - notbuy > exp)
				break;
			else
				notbuy = buy;
		}
		cout << "Case #" << i << ": " << fixed << setprecision(7) << notbuy << endl;
	}

	return 0;
}