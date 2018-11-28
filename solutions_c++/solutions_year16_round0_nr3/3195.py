#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int t;
int n, m, a[11];
vector<int> ans;
inline int prime(long long x)
{
	if ((x&1)==0)
		return 2;
	for(long long i = 3; i*i<=x; i += 2)
		if (x % i == 0)
			return i;
	return -1;
}
int main ()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("output.txt");
	cin >> t;
	for(int test = 1; test <= t; ++test)
	{
		cin >> n >> m;
		cout<<"Case #1:\n";
		for(int mask = (1<<(n-1))+1; mask < (1<<n); mask += 2)
		{
			int p=0;
			for(int j=2; j<=10;++j)
			{
				long long dx = mask, x = 0;
				for(int i = n-1; i>=0; --i)
					if (mask&(1<<i))
						x=x*j+(mask&1);
					else x = x*j;
				p = prime(x);
				if (p==-1)
					break;
				a[j-2]=p;
			}
			if (p==-1)
				continue;
			for(int j = n-1;j>=0;--j)
				cout<<((mask&(1<<j))!=0);
			for(int i=0;i<9;++i)
				cout<<" "<<a[i];
			cout<<endl;
			m--;
			if (m==0)
				return 0;
		}
	

		cout<<"\n";
	}
} 