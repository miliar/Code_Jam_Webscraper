#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("0.in","r",stdin);
freopen("op.txt","w",stdout);
long long int t,i,j,l,c=0;
char input[10001];


cin>>t;
int counts=1;
	while(t--)
	{
		c=0;
		cin>>input;
		l = strlen(input);
		while(true)
		{
			i=0;
			if(input[i]=='-')
			{
				while(input[i]=='-' && i<l)
				{
					i++;
				}
				if(i==l)
				{
					c+=1;
					break;
				}
				else
				{
					
					for(int re=0;re<i;re++)
						input[re]='+';
					c+=1;
				}
 
			}




			else if(input[i]=='+')
			{
				while(input[i]=='+' && i<l)
				{
					i++;
				}
				if(i==l)
				{
					break;
				}
				else
				{
					
					for(int re=0;re<i;re++)
						input[re]='-';
					c+=1;
				}
			}

		}
		cout<<"Case #"<<counts<<": "<<c<<"\n";
		counts++;
	}
	return 0;
}
