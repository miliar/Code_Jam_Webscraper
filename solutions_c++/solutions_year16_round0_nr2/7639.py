#include <iostream>
int main()
{
	int t, fc, test=0;
	std::string stack;
	char sign;
	std::cin >> t;
	std::cin.ignore(32767, '\n');
	while(t--)
	{
		test++;
		fc=0;
		std::cin >> stack;
		int l=stack.length();
		sign=stack[0];
		for(int i=0; i<l-1 ; i++)
		{
			sign=stack[i+1];
			if(stack[i]!=stack[i+1])
				fc++;
		}
		if(sign=='-')
			fc++;
		std::cout << "Case #" << test << ": " << fc << std::endl;
	}
	return 0;
}