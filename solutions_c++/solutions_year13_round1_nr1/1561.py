#include <cstdio>
#include <sstream>
#include <vector>
#include <list>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <functional>
#include <cstdlib>
#include <stack>
#include <queue>
#include<deque>
#include <string>
#include <climits>
using namespace std;
//
#define pi 3.14159265
#define  print "Case #"<<t1<<": "
typedef unsigned long long uLL;
typedef long double LD;
typedef long long LL;
//
int fromDecimal(int n, int b){int r=0,m=0;while(n>0){r+=n%b*m; m*=10; n/=b;} return r;}
string fromDecimal2(int n, int b){  string chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";  string result=""; while(n>0) {  result=chars.at(n%b) + result; n/=b; }  return result;}
int toDecimal(int n, int b){ int r=0;int m=0; while(n>0){ r+=n%10*m; m*=b; n/=10; } return r; }
int GCD(int a, int b){ if (b==0) return a; return GCD(b,a%b);}
int LCM(int a, int b) {  return b*a/GCD(a,b); }
string DoubleToString(double val, string precession)
{
	char str[256];
	string format = "%" + precession;
	sprintf(str, format.c_str(), val);

	return string(str);
}
int ToInt(string data)
{
	int n;
	istringstream is( data );
	is >> n;

	return n;
}


double ToDouble(string data)
{
	double n;
	istringstream is( data );
	is >> n;

	return n;
}

bool isPrime(LL n)
{
	if(n <= 1) return false;
	if(n == 2 || n == 3) return true;
	if(n%2 == 0) return false;

	long long count = sqrt((double)n);
	for(long long i = 2; i <= count; i+=2)
	{
		if(n % i == 0)
			return false;
	}

	return true;
}

vector<LL> getPrimeNumberList(LL n)
{
	vector<LL> list;

	LL * sPrime = new LL [n + 1];
	fill_n(sPrime, n+1, 1);
	sPrime[0] = 0;
	sPrime[1] = 0;
	LL m = sqrt((double)n);

	for(LL i = 2; i<=m; i++)
	{
		if(sPrime[i])
		{
			for(LL k = i*i; k<=n; k+=i)
				sPrime[k] = 0;
		}
	}

	for(LL j = 0; j<=n+1; j++)
	{
		if(sPrime[j])
			list.push_back(j);
	}
	
	delete [] sPrime;

	return list;
}

vector<string> split(string str, char delim)
{
	vector<string> list;
	std::stringstream ss(str);
    std::string item;
    while (std::getline(ss, item, delim)) {
        list.push_back(item);
    }

	return list;
}

void main()
{
	freopen("input.txt","r",  stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1;t1<=T;t1++)
	{
		long long r,t;
		cin>>r>>t;
		long long count=0;
		for(int i=1; ; i+=2)
		{
			long long temp;
			temp=(r+i)*(r+i)-(r+i-1)*(r+i-1);
			if ((t-temp)>=0)
			{
				t=t-temp;
				count++;
			}
			else break;
		}
		cout<<print<<count<<endl;
	}//end of t
}