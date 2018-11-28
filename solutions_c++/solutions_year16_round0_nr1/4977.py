#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int T;
//	std::fstream IP("input.txt", std::ios_base::in);
	std::fstream IP("A-large.in", std::ios_base::in);
	IP>>T;
	std::fstream OP("OPlarge.txt", std::ios_base::out);
	int i,n,j;
	bool dig[10],flag;
	for(i=0;i<T;i++)
	{
		for(j=0;j<10;j++)
			dig[j]=false;
		IP>>n;
		flag=false;
		if(n!=0)
			for(j=1;flag==false;j++)
			{
				long long int c=j*n,temp;
				while(c!=0)
				{
					temp=c%10;
					dig[temp]=true;
					c=c/10;
				}
				flag=true;
				for(int k=0;k<10;k++)
					if(dig[k]==false)
						flag=false;
			}
		OP<<"Case #";
		OP<<i+1;
		OP<<": ";
		if(n!=0)
			OP<<(j-1)*n;
		else
			OP<<"INSOMNIA";
		OP<<"\n";
	}
	return 0;
}
