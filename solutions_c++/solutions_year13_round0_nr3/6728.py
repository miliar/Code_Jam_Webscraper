#include <cstdlib>
#include <vector>
#include <fstream>
#include <cmath>
#include <cstring>
#include <iostream>
#include <cstdio>
using namespace std;

bool isPalindrome(int check)
{
	char a[100];
	sprintf(a,"%d",check);
	//itoa(check,a,10);
	//char b[100];
	int i=0;
	//int j=0;
	while(a[i]!=NULL)
	{
		i++;
	}
	for(int k=0; k<i/2;k++)
	{
		if(a[k]!=a[i-k-1])
		{
			return false;
		}
	}
	return true;
	/*while(a[j]!=NULL)
	{
		b[i]=a[j];
		j++;
		i--;
	}
	for(int k=0;k<j;k++)
	{
		if(b[k]!=a[k])
		{
			return false;
		}
	}
	return true;*/
	
}
int main()
{
	ifstream ifile("C-small-attempt0.in");
	ofstream ofile("outputC.txt");
	int cases;
	ifile>>cases;
	for(int i=0; i<cases; i++)
	{
		int a,b;
		int num=0;
		ifile>>a;
		ifile>>b;
		for(int j=a; j<=b;j++)
		{
			if(isPalindrome(j))
			{
				float x = sqrt(j);
				if(x==static_cast<int>(sqrt(j)))
				{
					int z = x;
					if(isPalindrome(z))
					{
						num++;
					}
				}	
			}
		}
		ofile<<"Case #"<<i+1<<": "<<num<<endl;
	}
}
