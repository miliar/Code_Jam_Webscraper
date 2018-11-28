#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

vector<string> arr[1<<5];
vector<int> factors;

bool checkPrime(long long int n)
{
	for(int i=2;i*i<=n;i++)
		if(n%i==0)
		{
			factors.push_back(i);
			return 1;
		}
	return 0;
}

long long int getNum(string s, int base)
{
	long long int n = 0;
	for(int j=0;j<s.length();j++)
	{
		n *= base;
		n += s[j] - '0';
	}
	return n;
}

int checkPrimeForBases(string s)
{
	for(int i=2;i<=10;i++)
	{
		long long int n = getNum(s, i);
		if(!checkPrime(n))
			return i;
	}
	return 1;
}

long long int power(int base, int exp)
{
	long long int res = 1;
	for(int i=1;i<=exp;i++)
		res *= base;
	return res;
}

void precompute()
{
	int count = 0;
	vector<string> arr1; arr1.push_back("0"); arr1.push_back("1");
	for(int len=2;len<=14;len++)
	{
		int len1 = arr1.size();
		vector<string> arr2;
		for(int i=0;i<len1;i++)
		{
			arr2.push_back(arr1[i]+"0");
			arr2.push_back(arr1[i]+"1");
		}
		arr1 = arr2;
	}

	vector<string> arr2;
	for(int i=0;i<arr1.size();i++)
	{
		arr1[i] = "1" + arr1[i] + "1";
		arr2.push_back(arr1[i]);
		arr1[i] = arr1[i] + arr1[i];
	}

	for(int i=0;i<500;i++)
	{
		string s = arr1[i], s1 = arr2[i];
		cout << s << " ";
		for(int base=2;base<=10;base++)
		{
			long long int num1 = getNum(s1, base);
			cout << num1 << " ";
		}
		cout << endl;
	}

}


int main()
{

	cout << "Case #1: " << endl;
	precompute();
	return 0;
}