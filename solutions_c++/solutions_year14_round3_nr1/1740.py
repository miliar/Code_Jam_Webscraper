
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

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
typedef long long ll;
typedef complex<int> P;
typedef pair<int,int> pii;
const double EPS = 1e-10;
const double PI  = acos(-1.0);
template <class F, class T> void convert(const F &f, T &t){	stringstream ss; ss << f; ss >> t;}


bool solve(){
	int a, b;
	char c;
	cin>> a>> c>> b;
	
	double num = (double)a / b, num2 = 1.0 / b;
	int cnt = 0, cnt2 = 0;
	while(num < 1.0){
		num *= 2;
		cnt++;
	}
	while(num2 < 1.0){
		num2 *= 2;
		cnt2++;
	}
	int n = cnt2 + 1;
	vector<double> x(n);
	x[0] = 1.0;
	for(int i=1;i<n;i++){
		x[i] = x[i-1] / 2;
	}
	
	num = (double)a / b;
	for(int i=0;i<n;i++){
		while(num >= x[i]){
			num -= x[i];
		}
	}
	if(num < EPS) num = 0.0;
	
	if(num == 0){
		cout<< cnt<< endl;
	}else{
		cout<< "impossible"<< endl;
	}
	
	return true;
}

int main(){
	cout.setf(ios::fixed); cout.precision(10);
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1<< ": ";
		solve();
	}
	return 0;
}

 