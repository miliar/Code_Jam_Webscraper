#include <cstdio>
#include <iostream>
#define EP 1E-9
using namespace std;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("2outl.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int q = 1; q <= tc; q++) {
		double c,f,x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double rate = 2;
		double farm = 0;
		double cookiegentime = x/rate;
		double farmgentime = 0;
		double totaltime = cookiegentime + farmgentime;
	//	cout << totaltime << endl;
		while(1) {
			farmgentime += c/rate;
			farm++;
			rate += f;
			cookiegentime = x/rate;
			double temptime = cookiegentime + farmgentime;
	//		cout << temptime << endl;
			if (temptime - totaltime > EP) break;
			totaltime = temptime;	
		}
		printf("Case #%d: %lf\n", q, totaltime);
	}
}
