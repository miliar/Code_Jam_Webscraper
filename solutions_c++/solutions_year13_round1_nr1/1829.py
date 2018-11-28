
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <cctype>
#include <complex>
#include <vector>
#include <algorithm>

using namespace std;

double cir(double r){
	return M_PI*r*r;
}

int solve(){
	double r,t;
	cin>> r>> t;
	
	int ans=0;
	while(1){
		double need = 2*r + 1;
		if(need <= t){
			t -= need;
			ans++;
		}else{
			break;
		}
		r += 2;
	}
	
	return ans;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		int ans = solve();
		cout<< "Case #"<< i+1<< ": "<< ans<< endl;
	}

	return 0;
}

 