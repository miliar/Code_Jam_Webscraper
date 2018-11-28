/*
 * b.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: mamdouh
 */






#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("ansBL.out", "w", stdout);
	int t;
	cin>>t;
	for (int ii = 0; ii < t; ++ii) {
		double c, f, x;
		cin>>c>>f>>x;
		double ct = 0, cr=2;
		while(x / (cr + f) + c/cr < x/cr)
//			cout<<x / (cr + f) + c/cr<<" " << x/cr<<" "<<cr<< " "<< ct<<endl;
			ct+=c/cr, cr+=f ;

		printf("Case #%d: %.7f\n", ii+1, ct+x/cr);
	}
	return 0;
}
