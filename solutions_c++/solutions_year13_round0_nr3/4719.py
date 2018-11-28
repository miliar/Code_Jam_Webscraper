#include <fstream>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

typedef map<int,int> mii;
typedef pair<int,int> pr;
char ** t;

ifstream fin("c-large-1.in");
ofstream fout("outc.txt");

long long polim(long long c)
{
	long long resault = c;
	while (c)
	{
		resault = resault*10 + c%10;
		c/=10;
	}
	return resault;
}


long long polim1(long long c)
{
	long long resault = c;
	c/=10;
	while (c)
	{
		resault = resault*10 + c%10;
		c/=10;
	}
	return resault;
}

bool check(long long c)
{
	long long d = c;
	long long f = 10;
	int s = 1;
	while (f<d)
		f*=10,s++;
	f/=10;
	long long t = 1;
	while (f>t)
	{
		if ((c/f)%10 != (c/t)%10)
			return false;
		t*=10; f/=10;
	}
	return true;
}

int way(long long cur,long long &a, long long& b)
{
	int resault = 0;
	long long c = polim1(cur);
	long long c1 = polim(cur);
	c = c*c;
	if (c>b)
	{
		return 0;
	}
//	cout<<cur<<" "<<c<<" "<<c1<<endl;
	if (c>=a)
	{
		resault+=check(c);
	}
	c1 = c1*c1;
	if (c1>=a&&c1<=b)
	{
			resault+=check(c1);
	}
	for (int i=0;i<=3;i++)
	{
		if (cur!=0||i!=0)
			resault+=way(cur * 10 + i,a,b);
	}
	return resault;
}

int main()
{
	int t;
	fin >> t;
	for (int i=1;i<=t;i++)
	{
		long long a,b;
		fin>>a>>b;
		fout<<"Case #"<<i<<": "<<way(0,a,b);
		if ( i!=t )
			fout<<"\n";
	}
	fout.close();
	return 0;
}
