#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<utility>

using namespace std;

map<int, int> s;

int main()
{
	int t, i, n, c = 1, cnt, sum;
	cin>>t;
	while(t--)
	{
		cin>>n;
		char shy[n+1];
		cnt = 0;
		s.clear();
		for(i = 0; i <= n; i++) //i means shyness number
		{
			cin>>shy[i];
			s[i] += shy[i] - '0'; //string will never end in a 0
		}
		sum = s[0]; //number of ppl with shyness level 0
		//for(i = 0; i <= n; i++)
			//cout<<s[i]<<endl;
		for(i = 1; i <= n; i++) //i means shyness number
		{
			if(s[i] == 0)
				continue;
			else if(i <= sum and s[i] != 0)
			{
				sum += s[i];
				continue;
			}
			else
			{
				cnt += i - sum;
				sum += s[i];
				sum += cnt;
			}
		}
		cout<<"Case #"<<c++<<": "<<cnt<<endl;
	}
	return 0;
}				
