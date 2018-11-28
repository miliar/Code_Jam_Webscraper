#include <iostream>
using namespace std;

int main()
{
int t;
cin>>t;
int p=1;
int ans=0;
while(p<=t)
{
	int n,i,j;
	cin>>n;
	int a[n];
	int order[n];
	
	
	for(i=0;i<n;i++)
	{
		cin>>a[i];
		order[i]=i;
	}
	
	cout<<"Case #"<<p<<":";
	for(i=0;i<n;i++)
	{
		for(j=i;j<n;j++)
		{
			if(a[order[i]]<=a[order[j]])
			{
				int tmp=order[i];
				order[i]=order[j];
				order[j]=tmp;
				
			}
		}
	}
	
	
	while(a[order[0]]>0)
	{
		if(n==2 || (n>2 && a[order[2]]==0))
		{
		char ch=order[0]+65;
		cout<<" "<<ch;
		a[order[0]]-=1;
		ch=order[1]+65;
		cout<<ch;
		a[order[1]]-=1;		
		}
		else
		{
		char ch=order[0]+65;
		cout<<" "<<ch;
		a[order[0]]-=1;
		for(i=1;i<n;i++)
		{
			if(a[order[i]]>=a[order[i-1]])
			{
				int tmp=order[i];
				order[i]=order[i-1];
				order[i-1]=tmp;
			}
			else
			{
				break;
			}
		}
		
		}
	}
	cout<<endl;
	




p++;
}
return 0;
}
