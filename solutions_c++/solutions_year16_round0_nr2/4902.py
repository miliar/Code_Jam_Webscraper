#include <iostream>
#include <string>

int main()
{
	int t=0,n=0;
	std::string str0="a";
	std::cin>>t;
	for(int i=1;i<=t;++i)
	{
		std::cin>>str0;
		n=0;
		for(int j=0;j<str0.length()-1;++j)
		{
			if(str0[j]!=str0[j+1])
			{
				++n;
			}
			else
			{
				;
			}
		}
		if(str0[str0.length()-1]=='+')
		{
			std::cout<<"Case #"<<i<<":  "<<n<<"\n";
		}	
		else
		{
			std::cout<<"Case #"<<i<<":  "<<n+1<<"\n";;
		}
	}
	return 0;
}