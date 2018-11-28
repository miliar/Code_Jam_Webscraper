#include <iostream>
#include <string.h>
#include <stdio.h>
#include <conio.h>
using namespace std;

int main()
{
	int k,n,len,j,i;
	char str[1001],prev,output[1001];
	cin>>n;
	cin.get();
	for (j=1;j<=n;j++)//test case loop n times
	{
		cin.getline(str,1000);
		len=strlen(str);
		output[0]=str[0];
		for (i=1;i<len;i++)//test case loop n times
		{
			if(output[0]<str[i])
			{
				for(k=i;k>0;k--)
					output[k]=output[k-1];
				output[0]=str[i];
			}
			else if(output[0]==str[i])
			{
				for(k=i;k>0;k--)
					output[k]=output[k-1];
				output[0]=str[i];
			}
			else
			{
				output[i]=str[i];
			}
		}
		output[i]='\0';
		cout<<"Case #"<<j<<": ";
		puts(output);
	}
	return 0;
}

