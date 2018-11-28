#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;

string inBase2(long long n)
{	
	string ret = "";
	do
	{
		if(n%2==1)
			ret = "1" + ret;
		else
			ret = "0" + ret;
		n/=2;
	}while(n);
	
	return ret;
}

long long isPrime(long long n)
{
	
	for(long long i=2; i*i <= n; i++)
		if(n%i==0)
			return i;
	
	return 0;

}

long long convertToBase10(int n, int base)
{
	
	long long ret = 0;
	long long b = 1;

	do
	{
		if(n%2==1)
			ret += b;
		n/=2;
		b*= base;


	}
	while(n);
	
	return ret;
}


int main(int argc, char** argv)
{
long long a = 485432538631ll;

string fName = argv[1];
fstream In((fName+".in").c_str(), ios::in);
fstream Out((fName + ".out").c_str(), ios::out);

int tests;

In >> tests;


for(int h=0; h<tests; h++)
{
	int N, J;
	In >> N >> J;
	Out << "Case #" << h+1 << ": " << endl;

	for(int num=0x8001; J > 0 && num < 0x10000; num+=2)
	{
		vector<int> factors;
		int flag = true;
		for(int base=2; base < 11; base++)
		{
			long long  temp = convertToBase10(num, base);
				
			long long div = isPrime(temp);
			if(div != 0)
			{
				factors.push_back(div);
			}
			else
			{
				flag = false;
				break;
			}
		}
		if(flag)
		{
			cout << inBase2(num) << endl;
			for(int i=0; i<factors.size(); i++)
			{
				cout << convertToBase10(num, i+2) << " " << factors[i] << " " << isPrime(convertToBase10(num, i+2)) << endl;
			}
			cout << "--------------------" << endl;
			Out << inBase2(num) << " ";
			for(int i=0; i<factors.size(); i++)
				Out << factors[i] << " ";
			Out << endl;
			J--;
		}
	}

}

In.close();

Out.close();

return 0;

}
 
