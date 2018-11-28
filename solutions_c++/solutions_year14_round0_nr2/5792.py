#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <complex>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>

using namespace std;

double c, f, x;
double t[10000005];
int main()
{	
	int cases; cin >> cases;
	for (int ca = 1; ca <= cases; ca++) {
		cin >> c >> f >> x;
		
		for (int nb = 1; nb <= 10000000; nb++) {
			t[nb] = t[nb-1] + c/(2+(nb-1)*f);
		}
	
		//nb = number of buildings we'll buy
		double t_best = 1e99;
		for (int nb = 0; nb <= 10000000; nb++) {
			t_best = min(t_best, t[nb] + x/(2+nb*f));
		}
		cout << "Case #" << ca << ": " << setprecision(7) << fixed << t_best << endl;
	}
	return 0;
}