#include <iostream>
#include <string.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

using namespace std;

char flip (char cake)
{
char flipped;
	if (cake=='+')
		{
			flipped='-';
			return flipped;
		}
	if (cake=='-')
		{
			flipped='+';
			return flipped;
		}
	else 
		{
			cout<<"Flipping Error!";
			return 'z';
		}
}

int main()
{
	int n,i,j,k,len,count;
	char pancake[500];
	cin>>n;
	cin.get();
	for (i=1;i<=n;i++)//test case loop n times
	{
		count=0;
		cin.getline(pancake,500);
		len=strlen(pancake);
		for (j=1;j<len;j++)
			{
				if (pancake[j]!=pancake[0])
					{
						//flip
						count++;
						for (k=0;k<j;k++)
							{
								pancake[k]=flip(pancake[k]);
							}
					}
			}
			if (pancake[0]=='-')
				{
					count++;
					for (k=0;k<len;k++)
						{
							pancake[k]=flip(pancake[k]);
						}
				}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}