#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,i,j,k,fg;
	char s[1005];
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>s;
		j=k=0;
		while(j<strlen(s))
		{
			fg=0;
			if(s[j]=='+')
			{
				j++;
				while(s[j]=='+')
					j++;
				while(s[j]=='-')
				{
					j++;
					fg=1;
				}
				if(fg==1)
					k+=2;
			}
			else if(s[j]=='-')
			{
				j++;
				while(s[j]=='-')
					j++;
				k+=1;
			}
			//cout<<j<<endl;
		}
		cout<<"Case #"<<i<<": "<<k<<endl;
	}
	return 0;
}