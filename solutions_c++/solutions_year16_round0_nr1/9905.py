#include<bits/stdc++.h>
#include<iostream>
#include<string>
using namespace std;

string to_string(long long int n)
{
	string ans;
	while(n)
	{
		ans.push_back(n%10);
		n = n/10;
	}
	reverse(ans.begin(),ans.end());
	return ans;
}
int main()
{
	long long int i,j,k,l,m,n,t,x;
	cin >> t;
	for(k=1;k<=t;k++)
	{
		cin >> n;
		if(n==0)
		{
			cout << "Case #" << k << ": INSOMNIA" << "\n";
		}
		else
		{
			map<int,int>mymap;
			x = 1;
			while(mymap.size()!=10)
			{
				j = x*n;
				// cout << j << "\n";
				string s = to_string(j);
				for(i=0;i<s.size();i++)
					mymap[s[i]-'0']++;
				x++;
			}
			cout << "Case #" << k << ": " << j << "\n";
		}
	}
	return 0;
}