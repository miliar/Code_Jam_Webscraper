#include<iostream>
#include<fstream>
#include<string.h>
#include<cstring>
using namespace std;
int main()
{
	int a,b,cases,n;
	char s1[1000],s2[10000];
	scanf("%d",&cases);
	for(int k  =1;k<=cases;k++)
	{
		cin>>n;
		
		cin>>s1;
		cin>>s2;
		int len1 = strlen(s1);
		int len2 = strlen(s2);
		int count = 0;
		int flag = 0;
		for(int i=0,j=0;i<len1 || j<len2;)
		{
			if(s1[i]==s2[j])
			{
				i++;
				j++;
				
				
			}
			else if(s1[i-1]==s1[i] && i>=0)
			{
				i++;
				count++;	
			}
			else if(s2[j-1]==s2[j] && j>=0)
			{
				j++;	
				count++;
			}
			else
			{
				flag = 1;
				break;	
				
			}
			
			
		}
		if(flag==1)
		{
			cout<<"Case #"<<k<<": "<<"Fegla Won"<<endl;	
			
		}
		else
		cout<<"Case #"<<k<<": "<<count<<endl;
		
		
			
		
	}


cin.get();
cin.get();
return 0;
}
