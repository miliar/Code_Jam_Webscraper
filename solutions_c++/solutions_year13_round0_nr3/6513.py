#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int pali(int j)
{
	int temp=j,te1=0,te2=0;
	while(temp!=0)
	{
		te1=temp%10;
		te2=te2*10+te1;
		temp=temp/10;
	}
	if(te2==j)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
int main()
{
	ifstream fin;
	fin.open("C-small-attempt0.in");
	ofstream fout;
	fout.open("pans");

	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		int a,b,z=0,x,ag=0,ctr=0;
		float y,w;
		fin>>a>>b;
		for(int j=a;j<=b;j++)
		{
			z=pali(j);
			if(z==1)
			{
				y=sqrt(j);
				x=sqrt(j);
				w=y-x;
				if(w==0)
				{
					int ag;
					ag=pali(x);
					if(ag==1)
					{
						ctr++;
					}
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<ctr<<endl;
	}
	return 0;
}
