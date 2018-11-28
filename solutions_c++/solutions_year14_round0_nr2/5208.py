#include <iostream>
#include <cstdio>
using namespace std;

double C,F,X;

double ff(double c, double f, double t){
//	double tem;
	if( c/f + X/(f+F) < X/(f) ){
		t += c/f;	
		f += F;
		ff(c,f,t);
	}
	else
		return t += X/f;

}


int main(){
	int T,s=0;
	FILE *o = fopen("ansB.txt","w");
	scanf("%d",&T);
while(T--){
	double t = 0;
	scanf("%lf %lf %lf",&C,&F,&X);
	s++;

	fprintf(o,"Case #%d: %.7f\n",s, ff(C,2,t));	


}


return 0;
}
