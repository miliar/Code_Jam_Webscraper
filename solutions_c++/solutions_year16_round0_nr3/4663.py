#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <math.h>

using namespace std;

typedef long long llong;

void printBin(llong n)
{
	bitset<16> num(n);
	cout<< num;
}

bool isPrime(llong n, llong &divi)
{
	divi = -1;
	llong i;
	for(i=2; i*i<=n; i++)
	{
		if(n%i==0)
		{
			divi = i;
			return false;
		}
	}
	return true;
}

llong convBase(llong n, int b)
{
	llong res = 0;
	llong mul = 1;
	while(n>0)
	{
		int d = n%2;
		n /= 2;
		res += d*mul;
		mul *= b;
	}
	return res;
}

void solve(llong n, int j)
{
	int printed=0;
	llong last = (1<<n)-1;
	llong num = 1;
	num = num | (1<<(n-1));
	while(num<=last)
	{
		vector<int> vec;
		bool flag = true;
		for(int i=2; i<=10; i++)
		{
			llong inBase = convBase(num, i);
			llong divi;
			if(isPrime(inBase, divi)==true)
				flag = false;
			else
				vec.push_back(divi);
		}
		// cout<< endl;
		if(flag)
		{
			printBin(num);
			for(int i=0; i<vec.size(); i++)
				cout<< " " << vec[i];
			cout<< endl;
			printed++;
			if(printed==j)
				break;
		}
		num+=2;
	}
}

int main()
{
	int t, j;
	llong n;
	cin >> t;
	for(int i=1; i<=t; i++)
	{
		cin >> n >> j;
		cout<< "Case #" << i << ":" << endl;
		solve(n, j);
	}
}