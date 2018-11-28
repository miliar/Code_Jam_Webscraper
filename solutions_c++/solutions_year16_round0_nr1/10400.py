#include<iostream>
#include<fstream>
using namespace std;
#include<string.h>
long unsigned int check(long unsigned int n);
char a[10];
int main()
{
	ifstream fin;
	ofstream fout;
   	fin.open("A-large.in");
   	fout.open("output.out");
	int t,i;
	long unsigned int number[100],no;
	fin>>t;
	for(i=0;i<t;i++)
		fin>>number[i];
	for(i=0;i<t;i++)
	{
		memset(a, '\0', sizeof(a));
		if(number[i]==0)
		{
			fout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";
		}
		else
		{
			no=check(number[i]);
			fout<<"Case #"<<i+1<<": "<<no<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}

long unsigned int check(long unsigned int n)
{
	int count=0,i=1;
	long unsigned int n2=n;
	short unsigned int n1;
	while(1)
		{
			n1 = n2%10;
			if(a[n1]=='\0')
			{
				a[n1]=48+n1;
				count++;
			}
			if(count == 10)
			{
				printf("%ld\n",n*i);
				return n*i ;
			}
			n2=n2/10;
			if(n2==0)
			{
				i++;
				n2=n*i;
			}
		}
}
