#include<iostream>
#include<deque>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	
	char s[2000];
	int z=1;
	while(t--)
	{
		deque<char> q;
		cin>>s;
		int i,j;
		char ch;
		q.push_back(s[0]);
	    for(i=1;s[i];i++)
	    {
	    	if(s[i]>=q.front())
	    	q.push_front(s[i]);
	    	else
	    	q.push_back(s[i]);
		}
		cout<<"Case #"<<z<<": ";
		int size=q.size();
		for(i=0;i<size;i++)
		cout<<q[i];
		q.clear();
		cout<<"\n";
		z++;
	}
}
