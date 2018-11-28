#include <stdio.h>
#include <iostream.h>
#include <math.h>
#include <iomanip.h>


 double fun(long double c,long double f,long double x,long double s){
	long double res=(c/s)+(x/(s+f));
	if((x/s)<res){

return x/s;

	}

return (c/s)+(fun(c,f,x,s+f)) ;
}



int main(){
	int x,i;
	long double a,b,c,res,s;
	s=2.0;
	res=0.0;
	scanf("%d",&x);
	for(i=0;i<x;i++){
		scanf("%Lf %Lf %Lf\n",&a,&b,&c);
	//cout<<"here1";
		res=fun(a,b,c,s);
		cout<<setprecision(20)<<"Case #"<<i+1<<": "<<res<<"\n";
	}
	return 0;
}