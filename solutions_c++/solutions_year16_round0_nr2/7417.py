#include<iostream>
#include<string.h>
using namespace std;
int find_end(char a[],int end)
{
	int i,n=end;
	for(i=n;i>=0;i--)
	{
		if(a[i]=='+')
			end--;
		else break;
	}
	return end;
}

int checktop(char a[],int end)
{
	int i,end1=-1;
	for(i=0;i<end;i++)
	{
		if(a[i]=='+')
			end1++;
		else break;
	}
	return end1;
}	

void change(char a[],int end)
{
	int i;
	for(i=0;i<=end;i++)
	{
		if(a[i]=='-')
			a[i]='+';
		else
			a[i]='-';
	}
}

main()
{	
	int t,total,f,end,i;
	char a[100][101];
	cin>>t;
	for(i=0;i<t;i++)
		cin>>a[i];
	
	for(i=0;i<t;i++)
	{
		total=0;
		end=strlen(a[i])-1;
		while(1)
		{
			end=find_end(a[i],end);
			if(end==-1)
				break;	
			f=checktop(a[i],end);
			if(f!=-1)
			{	change(a[i],f);
				total++;
			}
			change(a[i],end);
			total++;
		}
		cout<<"Case #"<<i+1<<": "<<total<<"\n";
	}
}
