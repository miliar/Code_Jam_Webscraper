// Cookie Clicker Alpha.cpp : 定义控制台应用程序的入口点。
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
using namespace std;

int main(int argc, char* argv[])
{
	FILE* fp;
	freopen_s(&fp, "B-large.in", "r", stdin );
	freopen_s(&fp, "B-large.out", "w", stdout );

	int n;

	cin >> n;
	
	for(int caseN = 1; caseN <= n; ++caseN)
	{
		double c, f, x;

		cin >> c >> f >> x;
		double speed = 2;
		double totalTime = 0;
		while( 1 )
		{
			double cost = c / speed;
			if( cost + x / (speed + f) < x / speed )
			{
				speed += f; 
				totalTime += cost;
			}
			else break;
		}

		totalTime += x / speed;

		printf_s("Case #%d: %.7f\n", caseN, totalTime );
	}

	return 0;
}

