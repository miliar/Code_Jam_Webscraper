#include<iostream>
#include<string.h>
using namespace std;

int main()

{
	int tttt=0;
	cin>>tttt;
	int cases=1;
	long long int count=0,temp=0;
	int n=0;
	string s;
	bool flag=false;
	int length;
	int init,last=0;
	while(cases<=tttt)
	{
		count=0;temp=0;
		int j=0;
		cin>>s>>n;
		length=s.length();
		last=-1;
		for(int i=0;i<length;i++)
		{
			if(s[i]!='a'&&s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u')
			{
				init=i;
				j++;
				i++;
				while(i<length && s[i]!='a'&&s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u')
				{
					j++;
					i++;
				}
				//if(i==length)i--;
				if(j>=n)
				{
					count+=((init-last)*(length-init-n+1));
					
				
					if(j>n)
					{
						j--;
						while(j>=n)
						{
						init++;
						count+=(length-init-n+1);
						j--;
						}
					}
					last=init;
				}
				j=0;


			}
		}
		cout<<"Case #"<<cases<<": "<<count<<endl;
		cases++;
	}
	return 0;

}