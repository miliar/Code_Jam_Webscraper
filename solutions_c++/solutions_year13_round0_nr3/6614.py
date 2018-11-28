#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <math.h>

using namespace std;

int isps(int n)
{
	int m;
	float p;
	p=sqrt(n);
	m=p;
	if(p==m)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
int ispal(int num)
{
    int rem,sum=0,numCopy;    //Defining variables.
    numCopy=num;
 
    while(num!=0)    //Loop to reverse the number.
    {
        rem=num%10;
        num=num/10;
        sum=sum*10+rem;
 
    }
 
    //Result Display:
    if(numCopy==sum)
    {
        return 1;
    }
    else
 
    {
        return 0;
    }
}
int ispalsq(int a,int b)
{
	int j=0;
	int c=0;
	for(int i=a;i<=b;i++)
	{
		if (ispal(i)==1)
		{
			if(isps(i)==1)
			{
				j=sqrt(i);	
				if (ispal(j)==1)
				{
					c++;
				}
			}	
		}
	}
	return c;
}
int main()
{
	int t,x,y,r,z=1;
	ifstream fin;
	fin.open("C-small-attempt1.in",ios::in);
	ofstream fout;
	fout.open("output.txt",ios::out);
	fin>>t;
	char ch;
	while(!fin.eof())
	{
		fin>>x;
		fin>>y;
		r=ispalsq(x,y);
		fout<<"Case #"<<z<<": "<<r;
		z++;
		if(z<=t)
		{
			fout<<"\n";
		}
		else
		{
			break;
		}	
	}
	fin.close();
	fout.close();
	cout<<"\nPress any key to EXIT..";	
	getch();
	return 0;
}
