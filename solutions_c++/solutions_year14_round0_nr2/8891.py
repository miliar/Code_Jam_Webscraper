#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

double func(double P,double C,double X,double inc)
{
	if(X/P<(C/P)+X/(P+inc))
	return X/P;
	return min(X/P,(C/P)+func(P+inc,C,X,inc));
}

int main()
{
	int T;
	double C,F,X;
	double ans;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>C>>F>>X;
		ans=func(2.0000000,C,X,F);
    std::cout << std::fixed;
    std::cout << std::setprecision(7);
		cout<<setprecision(7);
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
