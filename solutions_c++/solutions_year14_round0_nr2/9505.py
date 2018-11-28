#include <bits/stdc++.h>
using namespace std;

double X,C,F;
	
double f(double R){
	if(X/R<C/R+X/(R+F)){
		return X/R;
	}
	return min(X/R,C/R+f(R+F));	
}

int T;

int main() {
	cin>>T;
	int caso=0;
	while(T--){
		cin>>C>>F>>X;
		printf("Case #%d: %.10f\n",++caso,f(2.0));
	}
	return 0;
}