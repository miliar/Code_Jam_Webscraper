#include <bits/stdc++.h>
using namespace std;

int main(){
	int tc;
	cin >> tc;
	for(int d=1;d<=tc;d++){
		double C, F, X;
		cin >> C >> F >> X;
		double currF = 2;
		double ans = 0;
		bool valid=true;
		while(valid){
			double buy;
			double nobuy;
			buy = (C/currF) + (X/(currF+F));
			nobuy =  X/currF;
			if(nobuy<buy){
				valid=false;
				ans += X/currF;
			}
			else{
				ans += C/currF;
				currF+=F;
			}
		}
		printf("Case #%d: %.7lf\n",d,ans);
		
	}
	return 0;
}
