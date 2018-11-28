#include <bits/stdc++.h>

using namespace std;

const double e = 1e-10;
double C, F, X;
int ntest;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> ntest;
	for (int test = 1; test <= ntest; test++) {
		cin >> C >> F >> X;
		double FF = 2;
		double t = 0;
		while (true) {
			double tt = C/FF;
			double t1 = tt + X/(FF + F);
			double t2 = X/FF;
			
			if (t1 < t2) {
				t += tt;
				FF += F;
			} else {
				t += t2;
				cout << "Case #" << test << ": "; 
				printf("%.7f\n", t);
				break;
			}
			
		}
	}
}
