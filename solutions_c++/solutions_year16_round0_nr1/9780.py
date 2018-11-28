//https://code.google.com/codejam/contest/6254486/dashboard

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool gotAllDigits(int n, vector<int> &v)
{
	for(int j=0;j<v.size();j++)
		if(v[j] == 0) return false;

	return true;
}

void storeDigitsInMap(long long int n,vector<int> &v)
{
	while(n!=0)
	{
		if(v[n%10] == 0)
			v[n%10] = 1;
		n = n/10; 
	}
}

int main()
{
	int t;
	cin >> t;
	int attempt = 0;

	while(attempt!=t)
	{
		vector<int> digitsMap(10,0); //initialize digit map to 0		
		int i=1;
		long long int n,number=0;
		cin >> n;
		attempt++;
		if(n==0)
			cout << "Case #" << attempt << ": " << "INSOMNIA" << endl;
		else
		{			
			while(!gotAllDigits(number,digitsMap))
			{
				number = n*i;
				storeDigitsInMap(number,digitsMap);
				i++;			
			}
			cout << "Case #" << attempt << ": " << number << endl;
		}		
	}
	return 0;
}