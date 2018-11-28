#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
#include <time.h>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("B-large.in");
    int cases;
    infile >> cases;
	double C; double F; double X;
    for(int iter=1; iter<=cases; iter++) {
        infile >> C >> F >> X;
		double rate = 2.0;
		double t_total = 0;
		//cout << "X: \t" << X << endl;
		while(X>0) {
			double t_to_C = C/rate;
			double t_to_X = X/rate;
			if(t_to_X < t_to_C) {
				t_total += t_to_X;
				break;
			}
			// IN ANY OTHER CASE, WILL GET TO C COOKIES
			t_total += t_to_C;
			X -= C; // X is now the gap btwn num cookies and input X
			double t_to_X_null = X/rate;
			double t_to_X_buy = (X+C)/(rate+F);
			if(t_to_X_buy < t_to_X_null) { // better to buy
				rate += F;
				X += C;
			}
		}
		printf("Case #%d: %.7f\n", iter, t_total);
    }
    infile.close();
    return 0;
}

