#include "stdafx.h"

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

int testcase()
{
	int r,w,c;
	cin >> r >> c >> w;
	int k = c / w;

	if ( c % w == 0 )
	{
		return k * (r - 1) + k + w - 1;
	}
	else
	{
		return k * (r - 1) + k + w;
	}
} 

int main()
{
	int n;
	std::cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		int r = testcase();
		std::cout << "Case #" << i+1 << ": " << r << std::endl;
	}
	
	return 0;
}