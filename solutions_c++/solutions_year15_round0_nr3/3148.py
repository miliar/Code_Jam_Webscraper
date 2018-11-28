#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
struct conv
{
	int den;
    char ch;
};
int mult(int a, int b)
{
	int arr[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
	if(a>0&&b>0)
	return arr[a-1][b-1];
	else if(a<0&&b<0)
	return arr[-a-1][-b-1];
	else if(a>0)
	return -arr[a-1][-b-1];
	else
	return -arr[-a-1][b-1];
}
int main()
{
	ifstream iff("abc.txt");
	ofstream off("answer.txt");
	conv hello[]={{1,'1'},{2,'i'},{3,'j'},{4,'k'}};
	char str[10003],str2[10003];
	int t,l,x,ans=1;
    iff>>t;
	for(int it=0;it<t;it++)
	{
		ans=1;
		int i;
		int flag=0;
		iff>>l;
		iff>>x;
		iff>>str;
		strcpy(str2,str);
		off<<"Case #"<<it+1<<": ";
		for(i=1;i<x;i++)
			strcat(str2,str);
			for(i=0;i<l*x;i++)
		{
			ans=mult(ans,hello[(int)(str2[i]-'h')].den);
			if(ans==2)
			{
				flag=1;i++;
				break;
			}
		}
		
		if(flag==0)
			off<<"NO\n";
		else
		{
			flag=0;ans=1;
			for(;i<l*x;i++)
			{
				ans=mult(ans,hello[(int)(str2[i]-'h')].den);
				
				if(ans==3)
				{
					flag=1;i++;
					break;
				}
			}
			
			if(flag==0)
				off<<"NO\n";
			else
			{
				flag=0;ans=1;
				for(;i<l*x;i++)
					ans=mult(ans,hello[(int)(str2[i]-'h')].den);
				if(ans==4)
					off<<"YES\n";
				else
					off<<"NO\n";
			}
		}
	}	
}
