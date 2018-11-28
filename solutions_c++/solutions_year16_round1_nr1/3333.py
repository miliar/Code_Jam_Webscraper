#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
int main()
{
	int b;
	
	string a;
	freopen("A-large (1).in","r",stdin);
	freopen("lol.out","w",stdout);
	cin>>b;
	for(int lel=1;lel<=b;lel++)
	{
		//cout<<"asd"<<endl;
		cin>>a;
		cout<<"Case #"<<lel<<": ";
		list<char> l;
		l.push_back(a[0]);
		for(int i=1;i<a.size();i++)
		{
			if(a[i]>=l.front())l.push_front(a[i]);
			else l.push_back(a[i]);
		}
		//cout<<"asd"<<endl;
		for(list<char>::iterator ii=l.begin();ii!=l.end();ii++)
		{
			cout<<*ii;
		}
		cout<<endl;
	}

}