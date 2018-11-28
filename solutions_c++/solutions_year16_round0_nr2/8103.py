#include<iostream>
#include<vector>
#include<string.h>
using namespace std;


int happy(char *str,int l)
{		
		int j=0;
		while(j<l)
		{
			if(str[j]=='+')
				j++;
			else
				break;
		}
		if(j==l)
			return 1;
		else 
			return 0;
}


int blank(char *str,int l)
{		
		int j=0;
		while(j<l)
		{
			if(str[j]=='-')
				j++;
			else
				break;
		}
		if(j==l)
			return 1;
		else 
			return 0;
}

int main()
{
	int t,i=1;
	cin >> t;
	while(i<=t)
	{
		char str[100];
		cin >> str;
		int l=strlen(str);
		int j=0,cnt=0;
		while(1)
		{
			if(happy(str,l))
				break;
			if(blank(str,l))
			{
				cnt++;
				break;
			}
			while(1)
			{	
				if(str[j]==str[j+1])
					j++;
				else
					break;
			}	
			for(int k=0;k<=j;k++)
			{	
				if(str[k]=='+')
					str[k]='-';
				else
					str[k]='+';
			}
			cnt++;

		}
		cout << "Case #" << i << ": " << cnt <<endl;
		i++;
	}
}
