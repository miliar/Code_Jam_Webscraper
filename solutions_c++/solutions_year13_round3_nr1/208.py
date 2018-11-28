#include <fstream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <list>
#include <set>
#include <map>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

bool isV(char ch)
{
	return ch == 'a' || ch == 'e' || ch =='i' || ch == 'o' || ch == 'u';
}

int n;
string s;
bool ok[1000005];
int nextOK[1000005];


long long solve()
{
	int i,j,c=0;
	long long ans = 0;
	
	for(i=0; i<s.length(); ++i)
	{
		if(isV(s[i]))
			c = 0;
		else
			++c;

		ok[i] = (c >= n);
	}

	nextOK[(int)s.length()-1]=-1;
	if(ok[s.length()-1])
		nextOK[(int)s.length()-1]=(int)s.length()-1;
	for(i=s.length()-2; i>=0; --i)
	{
		if(ok[i])
			nextOK[i] = i;
		else 
			nextOK[i] = nextOK[i+1];
	}

	for(i=0; (i+n-1)<(int)s.length(); ++i)
	{
		j=nextOK[i+n-1];
		if(j != -1)
		ans+=(long long)s.length()-j;
	}
	return ans;
}

int solve2()
{
	int i,j,k,c=0, ans=0;
	for(i=0; i<s.length(); ++i)
	{
		for(j=i; j<s.length(); ++j)
		{
			bool ok = false;
			c=0;
			for(k=i; k<=j; ++k)
			{
				if(isV(s[k]))
				{
					if(c>=n)
					{
						ok = true;
						break;
					}
					c = 0;
				}
				else
					++c;
			}
			if(ok || c>=n)
				++ans;
		}
	}
	return ans;
}

int main()
{
	int t, tt;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>s>>n;
	/*	if(solve() != solve2())
		{
			cout<<"AAAAAAAAAAAAAAA";
			while(1);
		}*/
		fout<<"Case #"<<t<<": "<<solve()<<endl;
	}
	return 0;
}
