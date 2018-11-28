#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<iomanip>

using namespace std;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long a, b, k, sum,t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> a >> b >> k; 
		sum = 0;
		for(int j = 0; j < a; j++)
		{
			for(int o = 0; o < b; o++)
			{
				if((j&o) < k) sum += 1;



			}
		}
		cout << "Case #" << i << ": " << sum << endl;









	}
	
	return 0;



}