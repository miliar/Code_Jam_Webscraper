#include<iostream>
#include<iomanip>
#include<limits>
int main()
{
	int T;
	std::cin>>T;
	int n=T;
	while(T--)
	{
		double c,f,x,r=2.0;
		std::cin>>c>>f>>x;
		double t=0,y=x;
		while(x>0)
		{
// 			std::cout<<t<<' '<<x<<' '<<r<<std::endl;
// 			std::cin.get();
			double t_nb=x/r;
			double t_b=c/r+(x)/(r+f);
			
			if(x-c<0)
				t_b=std::numeric_limits<float>::max();
// 			std::cout<<t_nb<<' '<<t_b<<' '<<std::endl;
			if(t_nb<t_b)
			{
				x=0;
				t+=t_nb;
				break;
			}
			else
			{
				x=y;
				t+=(c/r);
// 				std::cout<<c/r<<std::endl;
				r+=f;
			}
		}
		std::cout<<std::fixed<<std::setprecision(7)<<"Case #"<<n-T<<": "<<t<<std::endl;
	}
	
}