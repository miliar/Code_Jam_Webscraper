#include <bits/stdc++.h>
using namespace std;
deque <char> d;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("A_large.out", "w", stdout);
    #endif // ONLINE_JUDGE
	int t;
	scanf("%d",&t);
	for(int p=1;p<=t;p++)
	{
		d.clear();
		string str;
		cin >> str;
		d.push_back(str[0]);
		for(int i=1;i<str.length();++i)
		{
			if(static_cast <int> (d.front()) > static_cast <int> (str[i]))
				d.push_back(str[i]);
			else
				d.push_front(str[i]);
		}
		deque <char> :: iterator it;
		cout<<"Case #"<<p<<": ";

		for(it=d.begin();it!=d.end();++it)
			cout<<*it;
		cout<<endl;
	}
}
