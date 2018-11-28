
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <queue>
#include <cctype>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <cassert>
#include <iomanip>

using namespace std;

#define dump(x)  cout << " "<< #x << " = " << (x) << endl;
#define pb push_back
#define all(x) (x).begin(),(x).end()
typedef long long ll;
typedef complex<int> P;
typedef pair<int,int> pii;
const double EPS = 1e-10;
const double PI  = acos(-1.0);




bool solve(){
	double c, f, x;
	cin>> c>> f>> x;
	
	double a = 2;
	double t = 0;
	double ans = x / a;
	for(int i=0;i<x;i++){	//
		t += c/a;
		a += f;
		ans = min(ans, t + x/a);
	}
	
	cout<< ans<< endl;
	return true;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);
	
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1<< ": ";
		solve();
	}
	return 0;
}

 