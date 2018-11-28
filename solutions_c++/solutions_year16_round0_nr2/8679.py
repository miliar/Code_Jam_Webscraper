#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
void flip(char *a,int length)
{
	for(int i=0;i<length;i++)
	{
		if(a[i]=='-')
		a[i]='+';
		else
		a[i]='-';
	}
}

int main()
{	 freopen("b1.in","r",stdin);
    freopen("bol.out","w",stdout);

	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{	int count =0;
		char ch[1000];
		cin>>ch;
		int l=strlen(ch);
		for(int j=l-1;j>=0;j--)
		{
			if(ch[j]=='+')
			continue;
			flip(ch,l);
			count++;
		}	
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}

return 0;
}

