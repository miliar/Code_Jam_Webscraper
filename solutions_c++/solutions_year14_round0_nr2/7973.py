#include <iomanip>
#include <algorithm>
#include <iterator>     // std::insert_iterator
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#define EPS 1e-11
using namespace std;
double C,F,X;

double solve(){
	double time = 0, rate = 2.0;
	double elapsed=0;
	while(X>0){
		double t1,t2;
		t1 = X/rate;
		if(X<C) return t1+elapsed;
		t2 = C/rate + X/(rate+F);
		if(t1 - t2 < EPS) return t1+elapsed;
		elapsed += C/rate;
		rate += F;
	}
}

int main(){
	ifstream in("A.in");
	ofstream out("result.txt");
	int TESTS,M; 
	in >> TESTS;
	for(int test = 0; test<TESTS; test++){
		cout << "Case #" << test+1 << ": ";
		out << "Case #" << test+1 << ": ";
		in >> C >> F >> X;
		double res = solve();
		  std::cout.setf( std::ios::fixed, std:: ios::floatfield ); 
		  out.setf( std::ios::fixed, std:: ios::floatfield ); 
		//printf("%.6lf\n",res);
		cout << res << endl;
		out	 << res << endl;

	}
	return 0;
}
