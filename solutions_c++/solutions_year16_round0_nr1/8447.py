#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out-A-large.out", "w", stdout);

	int testCases, n;
	long N, x, temp;
	bool goToSleep;
	cin >> testCases;
	for (int tc=0; tc < testCases; tc++) 
	{
		cin >> x;
		N = x;
		n = 1;
		goToSleep = false;
		vector<int> vec (10,0);
		if(x==0)
		{
			cout << "Case #" << tc+1 << ": " << "INSOMNIA" << endl;
		}
		else
		{
			while(1)
			{
				temp = N;
				do
				{
					vec[temp%10]++;
				}while(temp /= 10);
				goToSleep = true;
				for(int it1=0; it1 < 10; it1++)
				{
					if(vec[it1]==0)
					{
						goToSleep = false;
						break;
					}
				}
				if(goToSleep)
					break;
				n++;
				N = n * x;
			}	
			cout << "Case #" << tc+1 << ": " << N << endl;
		}
	}
	return 0;
}
