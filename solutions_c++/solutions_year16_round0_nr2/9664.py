#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

string s;

int main()
{
	int n;
	int i,j,k,l;
	bool b;
	char c='+';

	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>s;
		l=s.length();
		if(s[0]==c)
		{
			b=true;
		}
		else
		{
			b=false;
		}
		for(j=1,k=0;j<l;j++)
		{
			if(s[j]!=s[j-1])
			{
				k++;
				b=!b;
			}
		}
		if(b==false)
		{
			k++;
		}
		cout<<"Case #"<<i<<": "<<k<<endl;
	}

}
