#include<iostream>
#include<string.h>
#include<fstream>

using namespace std;
void rotate(char *a,int x);
int allplus(char *a);


int main()
{
	char a[105];
	int flag,j,l,x1,x2,c,plus,t,tt=1,count=0;
	ofstream myfile;
	myfile.open("Output2.txt");
	cin>>t;
	for(tt=1;tt<=t;tt++)
	{
	c=0;
	cin>>a;
	l=strlen(a);
	while(1)
	{
		flag=0;
		plus=0;
		x2=105;
		x1=105;
		if(allplus(a)==0)
		{
			myfile<<"Case #"<<tt<<": "<<c<<endl;
			break;
		}
		else if(allplus(a)==1)
		{
			myfile<<"Case #"<<tt<<": "<<c+1<<endl;
			break;
		}
		for(j=0;j<l;j++)
		{
	        if(a[j]=='-')
			flag=1;
			if(a[j]=='+'&&j!=0&&flag==1)
			{
			x1=j;
		    break;
		    }
		}
		flag=0;
		for(j=0;j<l;j++)
		{
		if(a[j]=='+')
			flag=1;
			if(a[j]=='-'&&j!=0&&flag==1)
			{
			x2=j;
		    break;	
		    }
        }
        if(x1<=x2)
        {
        rotate(a,x1);
        c++;
    }
        else
        {
        rotate(a,x2);
        c++;
    }
}
}
myfile.close();
return 0;
}

void rotate(char *a,int x)
{
	char c;
	int i;
	for(i=0;i<x-1;i++)
	{
		c=a[i];
		a[i]=a[i+1];
		a[i+1]=c;
	}
	for(i=0;i<x;i++)
	{
	if(a[i]=='+')
	a[i]='-';
	else
	a[i]='+';
	}
}
int allplus(char *a)
{
	int i,plus=0,min=0;
	for(i=0;i<strlen(a);i++)
	{
		if(a[i]=='+')
		plus++;
	else
	min++;
}
	if(plus==strlen(a))
	return 0;
	if(min==strlen(a))
	return 1;
}
