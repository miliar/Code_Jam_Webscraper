//the last word.cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,loop,len,n;
	char ch,chs;
	string s,s1;
	deque< char > d;
	deque< char >::iterator iter;
	scanf("%d",&t);
	getline(cin,s1);
	for(n=1;n<=t;n++)
	{
		getline(cin,s);
		len=(int)s.length();
		for(loop=0;loop<len;loop++)
		{
			ch=s.at(loop);
			if(loop==0)
			{
				d.push_back(ch);
				chs=ch;
			}
			else
			{
				if(ch >= chs)
					d.push_front(ch);
				else d.push_back(ch);
			}
			chs=d.front();
		}
		cout<<"Case #"<<n<<": ";
		iter=d.begin();
		for(;iter!=d.end();iter++)
			cout<<*iter;
		cout<<endl;
		s.clear();
		d.clear();
	}

	return 0;
}
