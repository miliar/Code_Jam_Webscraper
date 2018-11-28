// aa1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <random>
#include <map>
#include <set>
#include <time.h>
#include <iomanip>
using namespace std;





int _tmain(int argc, _TCHAR* argv[])
{
int i;
cin >>  i;
for (int q =1;q<=i;q++)
{
	double c,f,x;
	cin >> c >> f >> x;
	double start = 0.0;
	double speed  = 2;
	std::cout << std::setprecision(51);
	while (x > 0){
		if (x < c)
		{
			start += (x)/speed;
			break;
		}
		else
		{
			if ((x/(speed + f) +  c/speed) < (x)/speed)
			{
				start += c/speed;
				speed += f;
			}
			else
			{
				start += x/speed;
				break;
			}
		}
	}
	cout <<  "Case #" <<  q << ": " << start << std::endl;
}
}

