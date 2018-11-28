#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<math.h>

using namespace std;

int main()
{
	long long int r,t;
	int cases = 0;
	int number;
	cin >> number;
	for(int i = 0; i < number; i++)
	{
		cases++;
		cin >> r >> t;
		//long double rings = (-2*r-3+sqrt(4*r*r-4*r+8*t+9))/4;
		//long long int result = floor(rings);
		int i = 0;
		int rings = 1;
		int currentarea = 2*r+4*i+1;
		while(currentarea <= t)
		{
			i++;
			rings++;
			currentarea += 2*r + 4*i +1;
		}
		int result = rings -1;
		cout << "Case #" << cases << ": " << result << endl;
	}
}
