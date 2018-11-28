#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdint>

using namespace std;


int main(int argc, char** argv )
{
	int n;
	std::cin >> n; 
	for(int i = 0; i < n; ++i)   
	{
		int K;
		int C;
		int S;	
		std::cin >> K >> C >> S;
		std::cout << "Case #"<< std::to_string(i+1) << ": ";
		for(int j = 0; j < S; j ++)
		{
			cout << j+1 << " ";
		}	
		cout << endl;	
	}
    return 0;
}
