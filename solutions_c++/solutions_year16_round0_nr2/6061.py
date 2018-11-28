#include <bits/stdc++.h>
using namespace std;
typedef vector<char> vc;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("asd.txt","w",stdout);
	int a;
	cin>>a;
	for(int iex=1;iex<=a;iex++)
	{
		string b;
		cin>>b;
		int c=b.size();
		vector<char> v;
		int cont=0;
		for(int i=0;i<c;i++)
		{
			v.push_back(b[i]);
		}	
		char lol=v[0];
		for(vc::iterator ii=v.begin()++;ii!=v.end();ii++)
		{
			vc::iterator ie=ii;
			if(*ii!=lol)
			{
				cont++;
				reverse(v.begin(),ie--); 
				if(lol=='+')lol='-';
				else lol='+';
			}
		}
		if(lol=='-')cont++;
		cout<<"Case #"<<iex<<": "<<cont<<endl;



	}
}