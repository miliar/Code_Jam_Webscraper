#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>//deque<int> b;
#include <algorithm>//std::sort sort(b.begin(),b.end());
#define gc getchar_unlocked

using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
	int cases,c=1;
	deque<char> s;
	string in,ans;
	cin>>cases;
	while(c<=cases)
	{
		cin>>in;
		int x=0;
		s.push_back(in[x]);
		x++;
		while(x<in.length())
		{
			if(int(s.front())<=int(in[x]))
			{
				s.push_front(in[x]);
			}
			else
			{
				s.push_back(in[x]);
			}
			x++;
		}
		ans="";
		while(!s.empty())
		{
			ans=ans+s.front();
			s.pop_front();
		}
		cout<<"Case #"<<c<<": "<<ans<<"\n";
		c++;
	}
}