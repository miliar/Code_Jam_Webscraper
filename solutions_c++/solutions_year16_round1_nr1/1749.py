#include <iostream>
#include <cstdlib>
#include <string>
#include <deque>

using namespace std;

int main()
{
	int n;
	int i,j,k;
	int l,m;
	string s;
	deque <char> q;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>s;
		l=s.length();
		q.clear();
		q.push_back(s[0]);
		for(j=1;j<l;j++)
		{
			if(q[0]>s[j])
			{
				q.push_back(s[j]);
			}
			else
			{
				q.push_front(s[j]);
			}
		}
		cout<<"Case #"<<i<<": ";
		for(j=0;j<l;j++)
		{
			cout<<q[j];
		}
		cout<<endl;

	}
	return 0;
}
