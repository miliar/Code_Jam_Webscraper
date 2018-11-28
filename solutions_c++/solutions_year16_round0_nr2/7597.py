#include<iostream>
#include<string.h>
#include <stdio.h>
#include<cstdio>
using namespace std;

int main()
{

	long long int t,i,j,k;
	freopen ("ans2016-b.txt","w",stdout);
	freopen ("B-large.in","r",stdin);
	
	cin>>t;

	for(i=0;i<t;i++)
	{
		string s;
		char temp[100000];
		cin>>s;
		long long int index,count=0;
		index=s.size()-1;
		while(index>=0)
		{
			//If it is '+' then skip
			if(s[index]=='+')
			{
				index--;
				continue;
			}
			else
			{
				//i.e s[0] is '-'
				if(s[index]==s[0])
				{	
					//flipping bits from 0 to index
					for(k=0;k<=index;k++)
					{
						if(s[k]=='+')
						temp[k]='-';
						else
						temp[k]='+';
					}
					temp[k]='\0';
				
					//storing in reverse order
					for(k=0;k<=index;k++)
					{
						s[index-k]=temp[k];
					}
				
					//Decreasing index from end to first '-'
					while(s[index]=='+')
					{
						index--;
					}
				
				}
				else
				{
					//flipping bits from 0 till '-' comes
					k=0;
					while(s[k]=='+')
					{
						if(s[k]=='+')
						s[k]='-';
						else
						s[k]='+';
						k++;
					}
				}
				//Increment count of total no. of flips
				count++;
				
			}
		}	
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	
  	fclose (stdout);
	fclose(stdin);
	return 0;
}
