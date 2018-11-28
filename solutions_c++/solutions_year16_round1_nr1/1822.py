#include <bits/stdc++.h>

using namespace std;

int k = 1;
void solve()
{
	string s;
	cin>>s;
	std::vector<char> v;

	list<char> l;
	l.push_back(s[0]);
	for (int i = 1; i < s.length(); ++i)
	{
		if(s[i] < l.front())
			l.push_back(s[i]);
		else
			l.push_front(s[i]);
	}

	cout<<"Case #"<<k<<": ";
	list<char>::iterator x;
	for (x = l.begin(); x != l.end(); ++x)
	{
		cout<<*x;
	}
	cout<<endl;
	k++;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
		solve();
	return 0;
}