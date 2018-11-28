#include<iostream>
#include<stdio.h>
#include<cstring>

using namespace std;

int stringCompare(char str1[],char str2[]){
    int i=0,flag=0;
   
    while(str1[i]!='\0' && str2[i]!='\0'){
         if(str1[i]!=str2[i]){
             flag=1;
             break;
         }
         i++;
    }

    if (flag==0 && str1[i]=='\0' && str2[i]=='\0')
         return 1;
    else
         return 0;

}

int main()
{
	int t,i,j;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		char s[101],s2[101];
		cin>>s;
		int len=strlen(s)-1,count=0;
		while(len>=0)
		{
			
			while(s[len]=='+' && len>=0)
				len--;
			
			int temp=len,i=0;
			while(s[i]=='+' && len>0)
			{
				//cout<<temp<<"\n";
				s[i]='-';
				i++;			
			}
			if(i>0) count++;
			
			if(len>=0) count++;
			char s1[temp+1];
			for(j=0;j<=len;j++)
			{
				s1[j]=s[len-j];
			}
			s1[len+1]='\0';
			for(j=0;j<=len;j++)
			{
				if(s1[j]=='-')
					s[j]='+';
				else s[j]='-';
			}
			len--;
			//cout<<len<<"\n";
			//cout<<s<<"\n";
			
		}
		cout<<"Case #"<<i<<": "<<count<<"\n";
	}
}


















