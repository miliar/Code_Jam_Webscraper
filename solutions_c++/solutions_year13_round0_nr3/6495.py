#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<math.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;

bool ispal(int x)
{
	long long c = 0; bool f = 0;
	vector <int> arr;
	while(x != 0)
	{
		arr.push_back(x%10);
		x /= 10;
	}

	for(long long i=0 , j=arr.size()-1 ; i<arr.size() ; i++,j--)
	{
		if(arr[i] != arr[j]) 
		{
			f = 1;
			break;	
		}
	}
	if (f == 1) return 0;
	else return 1;
	
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	long long t , first , last;
	vector <long long> arr;
	cin >> t;

	for(long long k=1 ; k<=t ; k++)
	{
		long long counti = 0;
		cin >> first >> last;
		
		for(long long i= first ; i<= last ; i++)
		{
			if (ispal(i))
			{
				for(long long j = 0 ; j<= i ; j++)
				{
					if (ispal(j))
					if (j * j == i)
					counti ++;
				}
				
			}
				
			
		}
			
		cout << "Case #" << k << ":" << ' ' << counti << endl;
		counti = 0;
	}
	
	
	
}
