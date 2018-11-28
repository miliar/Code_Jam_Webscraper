#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <cctype>

#define limit 1000000
#define ull unsigned long long int

using namespace std;
/*
string toString(int n)
{
	stringstream ss;
	ss << n;
	return ss.str();
}*/


bool isPrime(int n)
{
	if(n <= 1)
		return false;
	else if(n < 4)
		return true;
	else if(n%2 == 0)
		return false;
	else if(n <9)
		return true;
	else if(n %3 == 0)
		return false;
	else
	{
		for(int i = 5; i <= floor(sqrt(n));i+=6)
		{
			if(n%i == 0) return false;
			if(n%(i+2) == 0)  return false;
		}
		return true;
	}
	
}

/*bool isPandigital(int n)
{

    string test = toString(n);
    sort(test.begin(), test.end());
    if(test != "1234567")
        return false;
    return true;

}*/


bool sieve[(limit-1)/2];
void EratostheneSieve()
{
	int n = limit;
	for(int i = 1; i < (ceil(sqrt(n))-1)/2;i++)
	{
		if(!sieve[i])
		{
			for(int j = 2*i*(i+1); j < (n-1)/2; j += (2*i)+1)
				sieve[j] = true;
		}
	} 
}
/*
int exp(int a, int b)
{
	int c = 2;
	for(int i = 0; i < b; i++)
		c*= a;

	return c;
}*/




int main() 
{
	
	int T = 0;
	cin >> T;

	for(int i = 0; i < T; i++)
	{
		
		int shyMax;
		cin >> shyMax;

		string aud;
		cin >> aud;
		
		int currShy = 0;	
		int nbAmi = 0;
	
		
		for(int j = 0; j <= shyMax; j++)
		{
			//cout << j << " " << currShy << endl;
			if(j <= currShy)
			{
				currShy += (int) (aud[j] - '0');
				
			}
			else if( (int) (aud[j] - '0') != 0)
			{
				nbAmi += j - currShy;
				currShy = j + (int) (aud[j] - '0') ;
				
			}
		}
		
		
		cout << "Case #" << i+1 << ": " << nbAmi << endl;

	}

	return 0;
}


