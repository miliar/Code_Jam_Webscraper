#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#define endl '\n'

using namespace std;

#define lli long long int

double d[100010];

int main() {
ios_base::sync_with_stdio(0);
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif	
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq + 1 << ": ";
		
		double c, f, x;
		cin >> c >> f >> x;


		double res = x / 2.0;
		d[0] = 0.0;
		for(int i = 1; i <= x; ++i) {
			d[i] = d[i-1] + c/(2.0 + f*(i-1));
			res = min(res, d[i] + x / (2.0 + f*i) );
		}
		printf("%.12lf", res);
		cout << endl;
	}
	return 0;
} 