#include <bits/stdc++.h>

using namespace std;

int main()
{
	list<char> l;
	string s;
	int i,t,len,j;
	cin >>t;
	for(i=0;i<t;i++)
	{
		l.clear();
		cin>>s;
		len=s.size();
		for(j=0;j<len;j++)
		{
			if(j==0)
				l.push_back(s[j]);
			else if (s[j]>=l.front())
				l.push_front(s[j]);
			else
				l.push_back(s[j]);
		}
		printf("Case #%d: ",i+1 );
		for(list<char>::iterator it=l.begin();it!=l.end();it++)
		{
			cout<<*it;
		}
 		printf("\n");	
	}

}