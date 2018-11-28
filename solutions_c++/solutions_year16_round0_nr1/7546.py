#include <iostream>
int main()
{
	int t, digits[10];
	int test=0;
	std::cin >> t;
	while(t--)
	{
		long c;
		test++;
		std::cin >> c;
		long n=c;
		int count=0, i=1;
		int sd;
		for(int j=0;j<10;j++)
			digits[j]=0;
		while(n>0)
		{
			sd=n%10;
			n=n/10;
			if(digits[sd]==0)
				{
					digits[sd]=1;
					count++;
				}
			if(n==0 && count <10)
			n=++i*c;
		}
		std::cout<<"Case #"<<test<<": ";
		if(c==0)
			std::cout << "INSOMNIA\n";
		else
			std::cout << i*c << "\n";
	}
	return 0;
}