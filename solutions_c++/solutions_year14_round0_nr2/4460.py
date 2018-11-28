#include <iostream>
#include <iomanip>
#include <vector>
#include <cassert>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

template<class T, class T1, class T2> inline bool Within(T x, T1 xMin, T2 xMax)
    {return (x >= xMin && x <= xMax);}

double Time(double C, double F, double X) {
    double t=0, n=0, v=2;
    if (C >= X)
	return X/v;
    while (n<X) {
	if (n<C) {
	    t += (C-n) / v;
	    n = C;
	}
	double wait = (X-n) / v;
	if (wait > C/F) {
	    n -= C;
	    v += F;
	}
	else
	   return t + wait;
    }
    return t;
}


int main() {
    int nTasks;
    cin >> nTasks;
    cout << setprecision(10);
    for (int iTask=1; iTask<=nTasks; iTask++) {
	double C, F, X;
	cin >> C >> F >> X;
	cout << "Case #" << iTask << ": " << Time(C, F, X) << '\n';
    }
}
