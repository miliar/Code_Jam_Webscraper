#include<iostream>
#include<cstring>
using namespace std;
char str[100];
void flip(long long int k)
{	
	long long int i;
	for(i=0;i<=k;i++)
	{
		if(str[i]=='-')
			str[i]='+';
		else
			str[i]='-';
	}
}
int main()
{	long long int T,l,j,i=1;
	long long int count=0;
	cin>>T;
	while(T--)
	{
		cin>>str;
		l=strlen(str);
		count=0;
		if(l==1)
		{
		   if(str[0]=='-')
		    {	
			count=1;
			str[0]='+';
		     }
		   else if(str[0]=='+')
			count=0;
		}
		else
		{	
			for(j=1;j<l;j++)
			{
				if(str[j-1]!=str[j])
				{
					flip(j-1);
					count++;
				}
			}
			if(str[j-1]=='-')
			{	flip(j-1);
				count++;
			}
		}
		//cout<<"\nstr is "<<str;
		cout<<"Case #"<<i<<": "<<count<<"\n";
		i++;
	}
	return 0;
}	
				
