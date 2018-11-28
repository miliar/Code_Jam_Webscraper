#include <iostream>
#include <iomanip> 
using namespace std;

int getK(double c, double f, double x){
	double tmp = (x/c-2/f-1);
	int res;
	if(tmp > 0)
		res = tmp+1;
	else
		res = 0;
	return res;
}

double getres(double c, double f, double x){
	double res;
	res = 0;
	int k = getK(c,f,x);
	for(int i = 0; i < k; i++){
		res += c/(2+i*f);
	}
	res += x/(2+k*f);
	return res;
}

int main(){
	int num;
	cin>>num;
	double res[100];
	for(int i = 0; i < num; i++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		res[i]=getres(C,F,X);
	}
	for(int i = 0; i < num; i++){
		cout<<setprecision(7) << setiosflags(ios::fixed | ios::showpoint)<<"Case #"<<i+1<<": "<<res[i]<<endl;
	}
}
