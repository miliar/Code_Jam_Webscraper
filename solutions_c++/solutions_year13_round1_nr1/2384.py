// Bullseye.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
using namespace std;

int compute(long r, long t) {
	return floor((sqrt((double)((2*r-1)*(2*r-1) + 8*t)) - (2*r-1))/4); 
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("d:\\A-small-attempt1.in");
	ofstream out("d:\\A-small-attempt1.out");
	int T = 0;
	in >> T;
	for(int i=1;i<=T;++i) {
		long r=0;
		long t=0;
		in >> r >> t;
		out << "Case #" << i << ": " << compute(r, t) << endl;
	}
	return 0;
}

