#include <bits/stdc++.h>
#define ll long long int
#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;
int main()
{
	/*std::vector<int> v({1,2,3});
	reverse(v.begin(),v.begin()+j);
    std::reverse(std::begin(v), std::end(v));*/
	int t,n,p,i,j,ans;
	char minus = '-';
	char plus='+';
	scanf("%d",&t);
	string s;
	p=t;
	while(p--)
	{
		int flag=0;
		cin >> s;
		n = s.size();
		vector<char> v;
		for(i=0;i<n;i++)
		{
			v.push_back(s[i]);
		}
		j=n-1;
		i=0;
		ans = 0;
		
		vector<char>::iterator it = v.end();
		vector<char>::iterator itr = v.begin();
		vector<char>::iterator itr1 = v.begin();
		while(flag==0)
		{
			int fl=0;
			while( it!=v.begin() && fl==0 )
			{
				if(*it == '-')
					fl=1;
				else
					it--;
			}
			if(it==v.begin())
			{
				if(*it == '-')
				{
					*it = plus;
					ans++;
				}
				flag=1;
			}
			else
			{
				if(*itr=='+')
				{
					itr1=itr;
					while(itr1!=it && *itr1 == '+')
					{	
						*itr1 = minus;
						itr1++;
					}
					ans++;
				} 

				if(*itr=='-')
				{	
					reverse(itr, it+1);
					for(itr1 = itr ; itr1!=it+1; itr1++)
					{
						if(*itr1=='-')
							*itr1 = plus;
						
						else 
							*itr1 = minus;
					}
					ans++;
				}
			}
		}

		printf("Case #%d: %d\n",t-p,ans);
	}
	return 0;
}