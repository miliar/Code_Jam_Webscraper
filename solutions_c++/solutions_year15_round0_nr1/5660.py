#include<bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int S;
		string str;
		cin>>S>>str;
		int f=0,p=0;
		for(int i=0;i<str.length();i++)
		{	if(p<i)
			{	f+=i-p;
				p+=i-p;}
			
				p+=str[i]-48;
		}
		printf("Case #%d: %d\n",t+1,f);
	}

	return 0;
}
