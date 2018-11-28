#include<bits/stdc++.h>
using namespace std;
int sum(int *shy,int n)
{
	int s=0;
	for(int j=0;j<n;j++)
		s+=shy[j];
	return s;
}


int main()
{
	int t;
	cin>>t;
	int num=1;
	while(t--)
	{
		int maxshy,people=0,maximum=0;
		cin>>maxshy;
		char s[maxshy+1];
		int shy[maxshy+1];
		cin>>s;
		for(int i=0;i<maxshy+1;i++)
		{
			shy[i]=s[i]-'0';
		}
		if(!maxshy)
		{
			cout<<"Case #"<<num<<" : 0"<<endl;
		}
		else
		{
			for(int i=0;i<maxshy+1;i++)
			{
				int a=sum(shy,i);
				//people=maximum(peolple,(i-a));
				people=i-a;
				if(people>=maximum)
					maximum=people;

			}
			if(maximum<0)
				maximum=0;
				cout<<"Case #"<<num<<": "<<maximum<<endl;
		}
		num++;

	}
	return 0;
}
