# include<iostream>
# include<string.h>
using namespace std;
int main()
{
	int t,j,l,i,n,pos,neg;
	char ch,str[105];
	cin>>t;
	for(j=1;j<=t;j++)
	{
		pos=neg=0;
		cin>>str;
		l=strlen(str);
		ch=str[0];
		if(ch=='+')
			pos=1;
		else neg=1;
		for(i=1;i<l;i++)
		{
			if(str[i]!=ch)
			{
				ch=str[i];
				if(ch=='+')
				{
					pos=neg+1;
				}
				else
				{
					neg=pos+1;
				}
			}
		}
		cout<<"Case #"<<j<<": "<<neg<<endl;
	}
	return 0;
}
