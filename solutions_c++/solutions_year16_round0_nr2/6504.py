#include <iostream>
#include <string.h>
using namespace std;

int all_happy(char *s)
{
	int length=strlen(s);
	while(length>=0)
	{
		if(s[length-1]=='-')
			return 0;
		length--;
	}
	return 1;
}

int all_blank(char *s)
{
	int length=strlen(s);
	while(length>=0)
	{
		if(s[length-1]=='+')
			return 0;
		length--;
	}
	return 1;
}

int main()
{
	int T,b;
	cin>>T;
	int i,count_minus=0,count_plus=0,first_plus=0,first_minus=0,flip=0,fliped=0,done=0,k=0;
	char s[101];
	char s1[101];
	for(i=0;i<T;i++)
	{
		flip=0;
		fliped=0;
		done=0;
		cin>>s;
		//flip=0;
		//s1=s;
		//cout<<"s="<<s<<endl;
		int length=strlen(s);
		/*int l=length;
		if(s[0]=='-')
			first_minus=1;
		else	
			first_plus=1;*/

		/*for(int j=0;j>l;j++)
		{
			if(s[j]=='-')
				count_minus++;
			else
				count_plus++;
		}*/
		while(!done)
		{
			if(all_happy(s))
				break;
			if(all_blank(s))
			{
				flip++;
				break;
			}
			if(s[0]=='-')
			{
				k=0;
				while(s[k]!='+')
				{
					fliped=1;
					s[k]='+';
					if(all_happy(s))
					{
						done=1;
						break;
					}
					k++;
					
				}
				//cout<<"s="<<s<<endl;
				if(fliped)
				{
					flip++;
					fliped=0;
				}
				
			}
			else
			{
				k=0;
				if(all_happy(s))
					break;
				//if(!all_happy(s))
					while(s[k]!='-')
					{
						fliped=1;
						s[k]='-';
						if(all_blank(s))
						{
							done=1;
							flip++;
							break;
						}
						
						k++;
						
					}
				//cout<<"s="<<s<<endl;
				if(fliped)
				{
					flip++;
					fliped=0;
				}
			}
			//cout<<"s="<<s<<endl;
		}

		
		cout<<"Case #"<<i+1<<": "<<flip<<endl;
		
		
	}
	return 0;
}