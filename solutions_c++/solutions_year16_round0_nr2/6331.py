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

int varcheck(string a)
{
	int ret=0;
	char prev;
	prev=a[0];
	int x=0;
	while(x<a.length())
	{
		if(a[x]!=prev)
		{
			ret++;
			prev=a[x];
		}
		x++;
	}
	if(prev=='-')
	{
		ret++;
	}
	return ret;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
	int cases,c=1;
	string a;
	cin>>cases;
	while(c<=cases)
	{
		cin>>a;
		cout<<"Case #"<<c<<": "<<varcheck(a)<<"\n";
		c++;
	}
}