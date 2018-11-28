#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char ch[1000];
void flip(int e)
{
	for(int i=0;i<e;i++)
	{
		if(ch[i]=='+')
			ch[i]='-';
		else
			ch[i]='+';
	}
}
int check()
{
	int f=0;
	for(int i=0;i<strlen(ch);i++)
	{
		if(ch[i]=='-')
		{
			return -1;
			f=1;
		}
	}
	if(f==0)
	{
		return 1;
	}
}

int main()
{
	int t;
	FILE *f;
	f=fopen("test2.txt","w");
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int count=0;
		cin>>ch;
		while(check()!=1)
		{
			int k=0;
			char v=ch[0];
			while(ch[k]==v)
				k++;
			flip(k);	
			count++;
		}
		//cout<<count<<"\n";
		fprintf(f,"Case #%d: %d\n",i+1,count);
		
	}
	
}
