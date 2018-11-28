# include<iostream>
# include<list>
# include<string.h>
using namespace std;
int main()
{
	int t,i,j,l;
	char str[1005];
	cin>>t;
	for(j=1;j<=t;j++)
	{
		list<char>a;
		list<char>::iterator it;
		cin>>str;
		l=strlen(str);
		a.push_back(str[0]);
		for(i=1;i<l;i++)
		{
			if((int)(str[i]-'A')>=(int)(a.front()-'A'))
				a.push_front(str[i]);
			else a.push_back(str[i]);
		}
		cout<<"Case #"<<j<<": ";
		for(it=a.begin();it!=a.end();it++)
		{
			cout<<*it;
		}
		cout<<endl;
		
	}
	return 0;
}
