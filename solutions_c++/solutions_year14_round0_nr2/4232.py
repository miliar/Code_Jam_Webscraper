#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;
typedef long long LL;

main() {
	FILE *fout = freopen("Blarge.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		double c, f, x;
		cin >> c >> f >> x;
		double mint = 100000000.0;
		double sum = 0.0;
		for(double i = 0.0; i <= 1000000.0; i+= 1.0){
			mint = min(mint, sum+x/(2+i*f));
			sum += c/(2.0+i*f);
		}
		printf("%.15lf\n", mint);
	}
	exit(0);
}