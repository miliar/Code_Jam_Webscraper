#include<iostream>
#include<string>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
	int t,ii;
	cin >> t;
	for(ii=0;ii<t;ii++)
	{
		int smax,i=0,count=0,req=0,standing=0;
		cin >> smax;
		string s;
		cin >> s;
		for(i=0;i<s.size();i++)
		{
			count = int(s[i]) - 48;
			if(standing >= i)
				standing += count;
			else
			{
				if(count != 0)
				{
					req = i - standing;
					standing += count;
				}
			}
		}
		cout << "Case #" << ii+1 << ": " << req << "\n";
	}

}
