#include <iostream>
#include <string>

int char2int(char c) { return c - '0'; }

int main()
{
	unsigned T;
	std::cin >> T;
	
	for(unsigned t=0; t<T; ++t)
	{
		unsigned Smax;
		std::cin >> Smax;
		
		std::string S;
		std::cin >> S;
		
		unsigned s = 0;
		unsigned v = 0;
		for(unsigned i=0; i<S.length(); ++i)
		{
			unsigned n = char2int(S[i]);
			
			if(i > s)
			{
				v += i - s;
				s += i - s;
			}
			
			s += n;
		}
		
		std::cout << "Case #" << (t+1) << ": " << v << std::endl;
	}
	
	return 0;
}
