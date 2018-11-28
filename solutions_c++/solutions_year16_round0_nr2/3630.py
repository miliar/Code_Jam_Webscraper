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
		string a;
		std::cin >> a;
		int pc = 0;
		char c = a[0];
		for(int j = 0; j < a.size(); ++j)
		{
			if (a[j] != c)
			{
				pc++;
				c = a[j];
			}
		}		

		if (c == '-')
			pc++;
		std::cout << "Case #"<< std::to_string(i+1) << ": " << std::to_string(pc) << endl;
	}
    return 0;
}
