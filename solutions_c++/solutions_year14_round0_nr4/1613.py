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

int T, N;

int cheat(set<double> A, set<double>B){

	int ret = 0;

	double a, b;
	while(A.size()){

		a = *(A.begin());
		b = *(B.begin());

		if(a < b){

			A.erase(a);
			B.erase(*(B.rbegin()));
		}
		else{
			A.erase(a);
			B.erase(B.begin());
			ret++;
		}
	}
	return ret;
}

int war(set<double> A, set<double>B){

	int ret = 0;
	while(A.size()){

		double a = *(A.begin());
		A.erase(a);


		set<double>::iterator it = B.lower_bound(a);

		if(it == B.end()){

			B.erase(B.begin());
			ret++;
		}
		else	B.erase(it);
	}

	return ret;
}

int main()
{
	cin >> T;

	for(int caseidx = 1; caseidx <= T; caseidx++){

		cin >> N;

		set<double>A;
		set<double>B;

		double t;

		for(int i = 0; i < N; i++){
			cin >> t;
			A.insert(t);
		}

		for(int i = 0; i < N; i++){
			cin >> t;
			B.insert(t);
		}
		printf("Case #%d: %d %d\n", caseidx, cheat(A, B), war(A, B));
	}

	return 0;
}

// vi: ts=2 sw=2
