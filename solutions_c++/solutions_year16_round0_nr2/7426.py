#include<iostream>
#include<cstring>
using namespace std;
void reverse(char *str,int len)
{
	int i=0,j=len;
	char temp;
	while(i<j)
	{
		temp=str[i];
		str[i]=str[j];
		str[j]=temp;
		i++;
		j--;
	}
	for(i=0;i<=len;i++)
	{
		if(str[i]=='+')
			str[i]='-';
		else
			str[i]='+';
	}
}
int main()
{
	int test,total;
	cin>>test;
	total=test;
	while(test--)
	{
		char s[100];
		cin>>s;
		int len=strlen(s)-1,i,j,count=0;
		for(i=len;i>=0;i--)
		{
			if(s[i]=='-')
			{
				j=0;
				while(s[j]=='+')
					j++;
				if(j!=0)
				{
					reverse(s,j-1);
					count++;
				}	
				
				reverse(s,i);
				count++;
			}
		}
		cout<<"Case #"<<total-test<<": "<<count<<endl;
	}
	
}
