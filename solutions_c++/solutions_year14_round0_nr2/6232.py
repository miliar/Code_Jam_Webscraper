#include<iostream>
#include<iomanip>
int main()
{
    int T;
    std::cin>>T;
    for(int i=0;i<T;++i)
    {
	long double s=2.0,c,f,x,result=0;
	std::cin>>c>>f>>x;
	while(1)
	{
	    if(x<=c)
	    {
		result+=x/s;
		break;
	    }
	    else if(x/s<c/s+x/(s+f))
	    {
		result+=x/s;
		break;
	    }
	    else
	    {
		result+=c/s;
		s+=f;
	    }
	}
	
	std::cout<<std::fixed<<std::setprecision(7);
	std::cout<<"Case #"<<i+1<<": "<<result<<'\n';
    }
}