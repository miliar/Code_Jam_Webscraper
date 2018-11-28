#include <iostream>
using namespace std;

int main()
{
	int t,k,c,s,i,j=1;
	std::cin>>t;
	while(t--)
	{
        std::cin>>k>>c>>s;
		std::cout<<"Case #"<<j<<": ";

		for(i=1;i<=k;i++)
		std::cout<<i<<" ";
		std::cout<<"\n";
		j++;
	}
	// your code goes here
	return 0;
}
