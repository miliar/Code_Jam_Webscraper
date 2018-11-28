#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main(){
	int t;
	cin >> t;
	int cse = 1;
	while(t--){
		
		double c, f, x;
		double ans = 0.0;
		cin >> c >> f >> x;
		double r = 2.00;
		while(1){
			if((double)(x/r) < ((double)(c/r) + (x/(r+f)))){
				ans += (double)x/r;
				break;	
			}
			else {
				ans += c/r;
				r = r + f;
			}
		}
		printf("Case #%d: %.7f\n",cse, ans);
		cse++;
	}
}
