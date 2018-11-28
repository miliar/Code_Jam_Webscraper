#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;

void optimize(char *&a)
{
	int index = 1;
	int index2 =0;
	char *b = new char;
	while(a[index2]!='\0')
	{
		index2++;
	}
	b[0] = a[0];
	for(int i=1;i<index2;i++)
		if(a[i-1]!=a[i])
		{
			b[index] =a[i];
			index++;
		}
	b[index]='\0';
	a = b;
	
	
}
int count(char *a,int n)
{
	int sum  =0;

	if(n==1)
		if(a[0]=='-')
			sum = 1;
		else if(a[0]=='+')
			sum = 0;
		else
		{
		}
	else	
	for(int i=n-1; i>=0; i--)
	{
		if(a[i]=='+')
		{
			if(i!=0)
			//dem day truoc do
			count(a,n-i);
			else
			{
			}
		}
		else if(a[i] =='-')
		{
			if(i!=0)
				sum +=2;
			else
				sum++;
		}

	}
	
	return sum;

}
void main()
{
	int n;
	char* a[1000];
	int b[1000];

	fstream f;
	f.open("B-small-attempt0.in",ios::in);
	f >> n;
	
	for(int i=0;i<n;i++)
	{
		a[i] =new char[1000];
		f >> a[i];
		
	}
	f.close();

	for(int i=0;i<n;i++)
	{
		optimize(a[i]);
	}

	for(int i=0;i<n;i++)
	{
		int index2 =0;
		while(a[i][index2]!='\0')
			{
				index2++;
			}
		b[i] = count(a[i],index2);
	}
	fstream f2;
	f2.open("B-small-attempt0.out",ios::out);
	for(int i=0;i<n;i++)
	{
		
		f2 << "Case #"<<i+1<<": "<<b[i]<<endl;
	}
	f2.close();

}
