#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
	int t,n;
	string s;
	cin>>t;
	for (int no = 1; no <= t; ++no)
	{
		cin>>n;
		cin>>s;
		int ovat = 0,count = 0,x;
		for (int i = 0; i <= n; ++i)
		{
			x = s[i] - '0';
			if(x>0 && count<i)
			{
				ovat += i - count;
				x += ovat;
			}
			count += x;
		}
		cout<<"Case #"<<no<<": "<<ovat<<endl;
	}
	return 0;
}