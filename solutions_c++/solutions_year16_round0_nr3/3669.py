#include <iostream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

long long power(long long base, long long exp)
{
	if (exp<=0) return 1;
	if (exp==1) return base;
	long long x=1;
	long long res=base;
	while(x<exp)
	{
		res = res*base;
		x++;
	}
	return res;
}

long long a[10];

string intToBinStr(int x,int len)
{
	string s;
	while(x>0)
	{
		if (x%2==1) s.push_back('1');
		else s.push_back('0');
		x /=2 ;
	}
	char c;
	for(int i=0;i<s.size()/2;i++)
	{
		c = s[i];
		s[i] = s[s.size()-1-i];
		s[s.size()-1-i]=c;
	}
	while(s.size()<len)	s = '0'+s;
	return s;
}

int main()
{
	int T, N, J;
	cin >> T;
	for(int z=0;z<T;z++)
	{
		cin >> N >> J;
		cout << "Case #" << z+1 << ": " << endl;
		string s;
		int nFound=0;
		long long number;
		vector<long long> nums;
		bool found=false;
		for(long long i=0;(i<power(2,N-2)) && (nFound<J);i++)
		{
			s.clear();
			s.push_back('1');
			s.append(intToBinStr(i,N-2));
			s.push_back('1');
			for(int j=0;j<10;j++) a[10]=0;
			nums.clear();
			for(int j=2;j<=10;j++)
			{
				number = stol(s,NULL,j);
				found=false;
				for(long long k=2;k<sqrt(number);k++)
				{
					if (number%k==0)
					{
						nums.push_back(k);
						found=true;
						break;
					}
				}
				if (!found) break;
			}
			if (nums.size()==9)
			{
				cout << s << " ";
				for(int y=0;y<nums.size();y++) cout << nums[y] << " ";
				cout << endl;
				nFound++;
			}
		}
	}
}