#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <boost/regex.hpp>

using namespace std;

typedef vector<string>::iterator vst;
typedef vector<int>::iterator vit;

bool isPal(long long a);
long long nextPal(long long a);

int main(int argc, char** argv)
{
	if(argc<2)
		exit(0);

	//file input
	ifstream in;
	in.open(argv[1]);

	int N = 0;
	in >> N;

	for(int _i=0; _i<N; _i++)
	{
		cout << "Case #" << _i+1 << ": ";

		long long n,m,palCount=0;
		in >> n >> m;

		//cout << sqrt(n) << " " << sqrt(m) << endl;
		long long i = sqrt(n);

		//cout << endl;
		//long long sum = 1;
		//for(long long i=a; i<=m; i+=sum)
		while(i*i<=m)
		{
			if( isPal(i*i) && isPal(i) && i*i>=n && i*i<=m )
			{
				palCount++;
				//cout << i << " " << i*i << endl;
			}

			//cout << i << " " << i*i << endl;

			if( isPal(i) )
				i = nextPal(i);
			else
				i++;
		}
		//cout << "palCount: " << palCount << endl;
		cout << palCount << endl;
	}

	in.close();
	return 0;
}

bool isPal(long long n)
{
	if(n<10)
		return true;

	long long a = 0, b = 0;
	a = n;

	while(n>0)
	{
		b *= 10;
		b += n%10;
		n/=10;
	}

	return a==b;
}

// Assuming the input is a palindrome
long long nextPal(long long n)
{
	if(n<10)
		return n+1;
	if(n<99)
		return n+11;

	long long sum, sum1, sum2, finalSum;
	long long p=0, m=n;
	bool bNines=true;

	vector<int> vNum;

	while(n>0)
	{
		vNum.push_back(n%10);

		if(n%10 != 9)
			bNines = false;

		p++;
		n/=10;
	}


	sum = pow(10, ((int)p/2));
	sum1 = sum;//pow(10, ((int)p/2));
	sum2 = sum;//pow(10, ((int)p/2));
	//sum2 = pow(10, ((int)p/2)) + pow(10, ((int)p/2)-1);
	p /= 2;

	int nineCount = 0;
	for(int i=vNum.size()/2; i<vNum.size(); i++)
	{
		if(vNum[i] == 9)
		{
			nineCount++;
			p--;
		}
		else
		{
			break;
		}
	}

	sum2 = pow(10, ((int)p));
	sum1 = sum2 + pow(10, ((int)p)-1);

	if(bNines)
	{
		finalSum = 2;
	}
	else if(vNum.size()%2)
	{
		if(nineCount==0)
		{
			finalSum = sum;
		}
		else
		{
			//for(int i=0; i<nineCount; i++)
			//	sum1/=10;
			finalSum = sum1;
		}
	}
	else
	{
		if(nineCount>0)
			finalSum = sum2;

		finalSum = sum1;
	}

	//cout << m << " + " << finalSum << " = " << m+finalSum << endl;
	return m + finalSum;
}

