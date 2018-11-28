#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <numeric>
#include <ctime>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
#include <list>
#include <cstdio>

using namespace std;

int main()
{
		int caseNum;
		cin >> caseNum;

		for (int i = 0; i < caseNum; ++i)
		{
				int maxShy;
				cin >> maxShy;
				int minInv = 0;

				int a[maxShy + 1];
				for (int j = 0; j < maxShy + 1; ++j)
				{
						char c;
						cin >> c;
						a[j] = c - 48;
				}
				int currP = a[0];
				for (int j = 1; j < maxShy + 1; ++j)
				{
						if(j <= currP)
						{
								currP += a[j];
						}
						else if (a[j] != 0)
						{
								minInv += (j - currP);
								currP += (j - currP);
								currP += a[j];
						}
					
				}
				cout << "Case #" << i + 1 << ": " << minInv << endl; 

		}

		return 0;

}
