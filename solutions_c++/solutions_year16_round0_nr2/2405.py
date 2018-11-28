#include <iostream>
#define PLUS '+'
#define MINUS '-'
int main()
{
	int T;
	std::cin >> T;
	
	for(int i=0;i<T;i++)
	{
		std::string s;
		std::cin >> s;
		int ans = 0;
		for(int j=0;j<s.length();j++)
		{
			if (s[j]==PLUS)
			  continue;
			if (s[j]==MINUS)
			  {
                            if(j==0)
                              ans++;
                            else if(s[j-1]==MINUS)
                              continue;
                            else
                              ans+=2;  
			  }	
		}	
		std::cout << "Case #" << i+1 << ": " << ans << std::endl;	
	}
	return 0;
}
