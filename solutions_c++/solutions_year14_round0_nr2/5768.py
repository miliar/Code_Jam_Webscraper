#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
using namespace std;

#define rep(i,N) for((i) = 0; (i) < (N); (i)++)
#define rab(i,a,b) for((i) = (a); (i) <= (b); (i)++)
#define Fi(N) rep(i,N)
#define Fj(N) rep(j,N)
#define Fk(N) rep(k,N)
#define sz(v) (v).size()
#define all(v) (v).begin(),(v).end()

int main() {
	int T,cs;
	double C,F,X;
	double time,i,p,q;
	double d;

	cin >> T;

	rab(cs,1,T) {
		cin >> C >> F >> X;

		time = 1e+30;
		p = 0;
		d = 2;

		for(i = 0; p < time; i++) {
			q = p + (X / d);
			if(q < time) time = q;
			//cout << time << endl;

			p += (C / d);
			d += F;
		}

		printf("Case #%d: %.7lf\n",cs,time);
	}
	return 0;
}
