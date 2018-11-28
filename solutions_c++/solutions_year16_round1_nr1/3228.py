#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int t1=1;t1<=t;t1++)
	{
		string s;
		cin>>s;
		int n=s.length();
		deque<char> r;
		r.push_front(s[0]);
		for(int i=1;i<n;i++)
		{
			if(r.front()>s[i])
			{
				r.push_back(s[i]);
			}
			else
			r.push_front(s[i]);
		}
		cout<<"Case #"<<t1<<": ";
		for(int i=0;i<n;i++)
		{
			char t=r.front();
			cout<<t;
			r.pop_front();
		}
		cout<<endl;
	}
}
