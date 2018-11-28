#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int t;
cin>>t;
char ch;
char s[10000];	
int m=1,h,len,f=-1;
for(m=1;m<=t;m++)
{	
	cin>>s;
	char res[1000]="\0";
	char temp[1000];
	temp[0]=s[0];
	temp[1]='\0';
	strcat(res,temp);	
	for(int i=1;i<strlen(s);i++)
	{
		if(s[i]>=res[0])
		{
			temp[0]=s[i];
			temp[1]='\0';
			strcat(temp,res);
			strcpy(res,temp);
			
		}
		
		else
		{
			temp[0]=s[i];
			temp[1]='\0';
			
			strcat(res,temp);
			
		}
	}
	
	cout<<"Case #"<<m<<": "<<res<<endl;
}

return 0;
}	
