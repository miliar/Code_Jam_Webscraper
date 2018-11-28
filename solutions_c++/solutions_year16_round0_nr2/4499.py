#include<iostream>
#include<string.h>
using namespace std;

void xxx(char a[])
{
	cout<<"Stack : "<<a<<endl;
}

void change(char a[] , int x)
{
	for(int i=0;i<=x;i++)
	{
		if(a[i] == '+')
		a[i] = '-';
		else
		a[i] = '+';
	}
	
	//cout<<"before rev : "<<a<<endl;
	
	for(int i=0;i<=x/2;i++)
	{
		char temp = a[i];
		a[i] = a[x-i];
		a[x-i] = temp;
	}
	
	//cout<<"after rev : "<<a<<endl;
}

long steps = 0;

void perform(char a[],int i)
{
	if(a[i] == '+')
	return ;
	
	else
	{
		long index = -1,k;
		for(k=0;k<i;k++)
		{
			if(a[k] == '+')
			{
				index++;
			}
			else 
			{
				break;
			}
		}
		
		if(index >= 0)
		{
			steps++;
			change(a,index);
		}
		
		steps++;
		change(a,i);
	}
	//xxx(a);
}

int main()
{
	int t;
	cin>>t;
	int casee = 1;
	while(t--)
	{
		char a[100] = "";
		cin>>a;
		steps=0;
		for(int i=strlen(a)-1;i>=0;i--)
		perform(a,i);
		cout<<"Case #"<<casee++<<": "<<steps<<endl;
	}
}
