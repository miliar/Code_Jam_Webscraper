#include<iostream>
using namespace std;
#include <iomanip>

int main()
{
	double get();
	int t,i;
	cin>>t;
	double a[t];
	for(i=0;i<t;i++)
	{
		a[i]=get();
	}
	for(i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		std::cout << std::fixed;
  		std::cout << std::setprecision(7) << a[i] <<endl;
  	}
  	
  	return 0;
}
double get()
{
	double c,f,x,y=2,s=0;
	cin>>c>>f>>x;
	double time=x/y;
	while(time>((c/y)+x/(f+y)))
	{
		s+=c/y;
		y=f+y;
		time=x/y;
	}
	return (s+time);
}