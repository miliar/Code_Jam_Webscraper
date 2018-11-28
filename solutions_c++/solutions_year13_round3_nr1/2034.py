#include<iostream>
#include<string.h>

using namespace std;

int main()

{
	int t=0;
	cin>>t;
	int comp_sci=1;
	long long int cnt=0,temporary=0;
	int n=0;
	string s;
	bool flag=false;
	int length;
	int init,last=0;
	while(comp_sci<=t)
	{
		cnt=0;temporary=0;
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
					cnt+=((init-last)*(length-init-n+1));


					if(j>n)
					{
						j--;
						while(j>=n)
						{
						init++;
						cnt+=(length-init-n+1);
						j--;
						}
					}
					last=init;
				}
				j=0;


			}
		}
		cout<<"Case #"<<comp_sci<<": "<<cnt<<endl;
		comp_sci++;
	}
	return 0;

}
