#include <bits/stdc++.h>
#define ll long long 
using namespace std;

int main() {
	// your code goes here
	std::ios::sync_with_stdio(false);
	char s[1005],s1[1005],s2[1005];
	deque<ll>q;
	ll t,n,k=0,l=0,i,y=1;
	cin>>t;
	while(t--)
	{
		cin>>s;
		n=strlen(s);
		k=0;
		l=0;
		q.push_back(s[0]-'A');
		for(i=1;i<n;i++)
		{
			if(s[i]-'A'>=q.front())
			{
				q.push_front(s[i]-'A');
			}
			else
			q.push_back(s[i]-'A');
		}
		cout<<"Case #"<<y<<": ";
		
		while(!q.empty())
		{
			ll x=q.front();
			q.pop_front();
			cout<<char(x+65);
		}
		cout<<endl;
		y++;
	}
	

	
	return 0;
}
