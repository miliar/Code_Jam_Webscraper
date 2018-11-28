#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

long long int changes=0;
int testcase=0;
void change_content(char a[])
{
	bool flag=0;
	int i , loop_till=0;

	for(i=0;i<strlen(a);i++)
		if(a[i]=='-')
			flag=1;
	if(flag==0)
	{
		cout<<"Case #"<<(testcase+1)<<": "<<changes<<'\n';
		return;
	}
	else
	{
		for(i=0;i<strlen(a);i++)
		{
			if(i==0 && a[i]=='+')
			{
				int k=i;
				while(a[k]=='+' && k<strlen(a))
				{
					a[k]='-';
					k++;
				}
				changes++;
				
				// cout<<a<<'\n'<<1;
			}
			else if(i==1 && a[i]=='+'&& a[i-1]=='-')
			{
				loop_till=i-1;
			}
			else if(a[i-1]=='-' && a[i]=='+')
			{
				loop_till=i-1;
				flag=1;
			}
			else if(i==strlen(a)-1 && a[i]=='-')
			{
				flag=1;
				loop_till=i;
			}
		}

	// cout<<loop_till<<a<<'\n';
	char tempstr[101];

	for(i=0;i<=loop_till;i++)
		tempstr[i]=(a[loop_till-i]=='+')?'-':'+';

	for(i=0;i<=loop_till;i++)
		a[i]=tempstr[i];
	// cout<<a<<'\n'<<2;

	changes++;
	change_content(a);	
	}

}

int main()
{
	int t , i;
	cin>>t;

	for(i=0;i<t;i++)
	{
		testcase=i;
		string str;
		cin>>str;
		char a[100];
		int j;
		for(j=0;j<str.length();j++)
			a[j]=str[j];
		// fgets(a,101 , stdin);
		a[j]='\0';
		change_content(a);
		changes=0;
	}


	return 0;
}