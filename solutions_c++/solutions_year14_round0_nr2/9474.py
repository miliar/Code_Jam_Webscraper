#include <cstdio>
#include <iostream>
#include <iomanip>
int main()
{
	freopen( "input.in", "r", stdin);
	freopen( "output.txt", "w", stdout);
	int run;
	std::cin >> run;
	for( int test=1; test<=run; ++test)
	{
		long double ExpectTime=0, IncreaseRate=2;
		long double FramePrice, FrameProduceRate, Target;
		std::cin >> FramePrice >> FrameProduceRate >> Target;
		while( 1 )
		{
			if( Target/IncreaseRate < (FramePrice/IncreaseRate+ Target/(IncreaseRate+FrameProduceRate )) )
			{
				ExpectTime += Target/IncreaseRate;
				break;
			}else
			{
				ExpectTime += FramePrice/IncreaseRate;
				IncreaseRate += FrameProduceRate;
			}
		}

		std::cout << "Case #" << test <<": ";
		std::cout << std::setprecision(9);
		std::cout << ExpectTime << std::endl;
	}
}
