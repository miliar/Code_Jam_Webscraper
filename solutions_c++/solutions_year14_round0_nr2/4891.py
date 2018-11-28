#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
double C, F, X;
int main() {
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	int tc, t = 1;
	cin >> tc;
	while (tc--){
		cin >> C >> F >> X;
		double res = X / (double)2.0;
		double sum = 0, num_fram = 0;
		for (double i = 0; i < 10000; i++){
			res = min(sum + (X / (2.00 + (F*num_fram))), res);
			sum += (C / double(2.00 + F*(num_fram)));
			//cout << double(C/(2.00 + F*(num_fram))) << endl;
			num_fram++;
		}
		cout << "Case #" << t++ << ": " <<setprecision(7) << fixed << res << endl;
	}

}

