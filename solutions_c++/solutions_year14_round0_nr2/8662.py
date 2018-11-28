#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

double C,F,X;// C - Farm Cost
// F - Bonus Production
// X - Target Value

int cc = 0;
double solve(double f){
	if(f>=X)return X/f;
	double ret = solve(f+F)+C/f;
	if(ret < X/f)
		return ret;
	return X/f;
}

double solve(){
	double f = 2, t= 0;
	while (true)
	{
		double tf = C/f + X/(f+F);
		double tc = X/f;
		if(X/f <= C/f + X/(f+F)){
			t+=X/f;
			break;
		}
		else{
			t+=C/f;
			f+=F;
		}
	}
	return t;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin>>T;
	for (int z = 0; z < T; z++)
	{

		cin>>C>>F>>X;

		double o = solve();
		printf("Case #%d: %.7lf\n",z+1,o);
	}
}