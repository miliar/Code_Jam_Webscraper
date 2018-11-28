#include <iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
char s[101];
int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		memset(s,'0',sizeof(s));
		scanf("%s",&s);
		int countplus=0,countminus=0,count=0;
		//cout<<strlen(s);
		// for(int i=0;i<strlen(s);i++)
		// {
		// 	if(s[i]=='+')countplus++;
		// 	else countminus++;
		// }
		
		if(strlen(s)==countplus)
		{
			count=0;
		}
		else{
		//	cout<<"enter";
		for(int i=0;i<strlen(s)-1;i++)
		{
			
			if(s[i]=='-' && s[i+1]=='+')
			{
				count+=1;
				memset(s,'+',sizeof(char)*i);
				//s[i]='+';
			}
			else if(s[i]=='+' && s[i+1]=='-' )
			{
				count+=1;
				s[i]='-';
			}
			
		}
		}
		if(s[strlen(s)-1]=='-')count+=1;
		// for(int i=0;i<strlen(s);i++)
		// {
		// 	if(s[i]=='+')countplus++;
		// 	else countminus++;
		// }
		// if(strlen(s)==countminus)
		// {
		// 	count+=1;
		// }
		printf("Case #%d: %d\n",j,count);
		//cout<<j<<" "<<s<<" "<<count<<"\n";
	}
	return 0;
}