// 2013-1A-A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cmath>
#include <fstream>
#include <iostream>

typedef long long int64;
typedef long double float128;

using namespace std;

int64 test(int64 r, int64 t);

int _tmain(int argc, _TCHAR* argv[])
{
	ios_base::sync_with_stdio(false);

	ifstream in("A.in");
	ofstream out("A.out");

	int T;
	in >> T;

	for (int c = 1; c <= T; c++) {
		int64 r, t;
		in >> r >> t;

		int64 res = test(r, t);
		out << "Case #" << c << ": " << res << endl;
	}

	return 0;
}

int64 test(int64 r, int64 t)
{
	float128 rr = (float128)(r);
	float128 tt = (float128)(t);
	float128 dd = sqrt(4.0*rr*rr-4.0*rr+1.0+8.0*tt);
	float128 k = (dd-(2.0*rr+3.0))/4.0;

	int64 res = static_cast<int64>(k);

	if (2*res*res+res*(2*r+3)+2*r+1-t <= 0) {
		res++;
	}

	return res;
}


