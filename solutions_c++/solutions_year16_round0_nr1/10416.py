#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	long long N;
	cin >> t;
	vector<int> a(t);
	for (int i = 0; i < t; i++){
		cin >> a[i];
	}
	
	for (int i = 0; i < t; i++)
	{
		N = a[i];
		int b[10],j,flag=0;
		
		if (N==0)
		{
			cout << "Case #" << i + 1 << ": INSOMNIA"<<endl;
		}
		else
		{	
			long long k = N;
			for (j = 0; j < 10; j++)
			{

				b[j] = -1;
			}
			do
			{
				
			
			long long n = N;
			while (n>0)
			{
				int x = n % 10;
				b[x] = x;
				n /= 10;
			}
			for (j = 0; j < 10 ; j++)
			{
				if (b[j]!=j)
				{
					break;
				}
			}
			if (j==10)
			{
				cout << "Case #" <<i+1<< ": "<<N<<endl;
				flag = 1;
			}
			N = N + k;
			} while (flag==0);
			
		}
	}
	return 0;
}