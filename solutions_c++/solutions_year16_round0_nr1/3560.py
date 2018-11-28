#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv )
{
	int n;
	std::cin >> n; 
	for(int i = 0; i < n; ++i)   
	{
		int a;
		std::cin >> a;
		if ( a == 0 )
			std::cout << "Case #"<< to_string(i+1) << ": INSOMNIA" << endl;
		else
		{
			std::vector<bool> nb (10);
			int b = a;
			std::string s = std::to_string(b);
			bool fini = true;			
			while(fini)
			{
					
				fini = false;
				for (int j = 0; j < 10; ++j)
				if(!nb[j])
				{
					fini = true;
					nb[j] = ((int) s.find(std::to_string(j)) > -1);
				}
				b+= a; 
				s = to_string(b);
			}
			std::cout << "Case #"<< std::to_string(i+1) << ": " << std::to_string(b - 2*a) << endl;
		}
	}
    return 0;
}
