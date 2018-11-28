#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	int T;
	string s;
	int len,i,cnt,flag=0,j;
	cin>>T;
	for(j=1;j<=T;j++)
	{
		cnt=0;
		flag=0;
		cin>>s;
		len=s.length();
		if(s[0]=='-')flag=1;
		for(i=0;i<len;i++)
		{
			if(s[i]=='-')
			{
			while(s[i]=='-' && i<len)
			{
				i++;
			}
			cnt+=2;
			}

		}
		if(flag==1)cnt--;
		cout<<"Case #"<<j<<": "<<cnt<<"\n";
	}
	return 0;
}