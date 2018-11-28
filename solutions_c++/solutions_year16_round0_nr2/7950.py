#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	ios::sync_with_stdio(0);
	int t,c=1;
	cin>>t;
	while(c<=t)
	{
		string str="";
		cin>>str;
		int l=str.length();
		char ch;
		int count=0;
		if(str[0]=='+')
			ch='+';
		else
			ch='-';
		for(int i=1;i<l;i++)
		{
			if(str[i]!=ch)
			{
				count++;
				if(ch=='+')
					ch='-';
				else
					ch='+';
				i--;
			}
		}
		if(ch=='-')
			count++;
		cout<<"Case #"<<c<<": "<<count<<endl;
		c++;
	}
	return 0;
}