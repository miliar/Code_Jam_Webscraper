/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

using namespace std;

typedef long long LL;
typedef complex<double> point;
typedef long double ldb;
typedef pair<int,int> pii;

LL N,p;

inline LL checkMin(LL tot, LL len){
	if (len==1)
		return tot-1;
	return checkMin(tot/2, len/2);
}

inline LL checkMax (LL tot, LL len){
	if (len==1)
		return (1LL<<N) - tot;
	return checkMax(tot/2, len/2);
}

inline void main2(){
	cin >> N >> p;
	LL ansMin = 0, ansMax=0;
	LL lo = 0, hi = (1LL<<N)-1;
	while (lo<=hi){
		LL mid = (lo + hi) / 2;
		if (checkMin((1LL<<N), (1LL<<N)-mid)<p){
			ansMax = mid;
			lo = mid+1;
		}else{
			hi = mid-1;
		}
	}
	lo = 0, hi = (1LL<<N)-1;
	while (lo<=hi){
		LL mid = (lo + hi) / 2;
		if (checkMax(1LL<<N, mid+1) < p){
			ansMin = mid;
			lo = mid+1;
		}
		else
			hi = mid-1;
	}
	cout << ansMin << ' ' << ansMax << endl;
}

int main(){
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
