#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <iomanip>

#ifdef _WIN32
#define LL "%I64d"
#else
#define LL "%lld"
#endif

#define inp(x) scanf("%d",&x)
#define inpf(x) scanf("%f",&x)

using namespace std;

typedef long long int ll;
typedef long long unsigned int ull;

int main() {
	int T;
	int n;
	double C,F,X;
	double total_time;

	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> C >> F >> X;
		n = max(0,(int)((X*F - 2.0*C)/(F*C)));

		total_time = X/(2.0 + F*n);
		for (int i = 0; i < n; i++) {
			total_time += C/(2.0 + F*i);
		}

		cout << "Case #" << t << ": " << fixed << setprecision(7) << total_time << endl;
	}

	return 0;
}
