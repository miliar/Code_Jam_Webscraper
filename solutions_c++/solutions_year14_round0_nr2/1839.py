#include<sys/types.h>
#include<dirent.h>

#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<cassert>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<tr1/unordered_map>
#include<set>
#include<tr1/unordered_set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define lt(x, y)	((x) >= 0 && ((x) < (y) || (y) < 0))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

double C, F, X;

int main()
{
	int T;

	cin >> T;

	for(int caseidx = 1; caseidx <= T; caseidx++){

		cin >> C >> F >> X;

		double t = 0;
		double v = 2.0;
		double ret = X / 2.0;

		if(C >= X)	goto end;

		while(t < ret){

			t += C / v;
			if(t >= ret)	break;

			v += F;
			double tt = t + X / v;
			ret = MIN(ret, tt);
		}


end:
		printf("Case #%d: %.7lf\n", caseidx, ret);
	}

	return 0;
}

// vi: ts=2 sw=2
