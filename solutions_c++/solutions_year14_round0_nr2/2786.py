#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <stdint.h>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <stdio.h>

using namespace std;


int main()
{

	int T; 
	cin >> T;
	
	for (int t=1; t<=T; t++)
	{
		double C,F,X;
		
		cin >> C;
		cin >> F; 
		cin >> X;
		
		double bestTime=1e10;
		double timeBuildingFarms=0;
		
		for (double numFarms=0; numFarms<100000; numFarms+=1)
		{
			double timeUsed=timeBuildingFarms+X/((numFarms)*F+2);
			if (timeUsed < bestTime)
			{
				bestTime=timeUsed;
			}
			timeBuildingFarms+=C/(numFarms*F+2);			
		}
		printf("Case #%d: %.7f\n", t, bestTime);
	}

}
