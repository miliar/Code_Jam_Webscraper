#include<bits/stdc++.h>
using namespace std;
char s[1100];
deque<char> q;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int a,b,c;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>a;
	for(b=0;b<a;b++)
	{
		cin>>s;
		q.push_back(s[0]);
		for(c=1;s[c];c++)
		{
			if(s[c]>=q.front())q.push_front(s[c]);
			else q.push_back(s[c]);
		}
		cout<<"Case #"<<b+1<<": ";
		while(!q.empty())
		{
			cout<<q.front();
			q.pop_front();
		}
		cout<<"\n";
	}
}
