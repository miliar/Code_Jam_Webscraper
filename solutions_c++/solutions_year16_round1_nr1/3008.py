#include<bits/stdc++.h>

using namespace std;

int main(void)
{
	int t,te;
	cin>>te;
	for(t=1;t <= te;t++)
	{
		string s;
		cin>>s;
		printf("Case #%d: ",t);

//		string s;
//		cin>>s;
		int i;
		deque<char> q;
		q.push_front( s[0]);
		char c;
		for(i=1;i<s.size();i++)
		{
			c = q.front();	
			if( s[i] >= c )	
			{
				q.push_front( s[i] );
			}
			else
				q.push_back( s[i] );
		}
		while( !q.empty())
		{
			cout<<q.front();
			q.pop_front();
		}
		cout<<endl;		
	}
	return 0;
}
