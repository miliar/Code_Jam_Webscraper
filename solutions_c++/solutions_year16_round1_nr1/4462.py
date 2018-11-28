#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<list>
using namespace std;
int main()
{	
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin != NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	char s[1000];
	int t;
	cin>>t;
	list<char> li;
	list<char>::iterator it;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>s;
		for(int j=0; j<strlen(s); j++)
		{
			if(j==0 || (j>0 && s[j]<li.front()))
					li.push_back(s[j]);
			else 
				li.push_front(s[j]);
		}
		for(it=li.begin();it!=li.end();it++)
			cout<<(*it);
		cout<<endl;
		li.clear();	
	}
	return 0;
}
