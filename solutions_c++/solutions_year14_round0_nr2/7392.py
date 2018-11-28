#include <iostream>
using namespace std;

double gao(double c,double f,double x,double s){	// s is speed
	if(x/s < (c/s)+ x/(f+s)){
		return x/s;
	} else {
		return (c/s) + gao(c, f, x, s+f);
	}
}
int main()
{
	int cnt;
	cin>>cnt;
	double c,f,x;
	for(int idx=1; idx <= cnt; ++idx){
		cin>>c>>f>>x;
		printf("Case #%d: %.7lf\n",idx, gao(c,f,x,2.0));
	}
	return 0;
}
