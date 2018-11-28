#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
char num[1000];
ifstream fin("C-small-attempt0.in");
ofstream fout("output.out");
int isP(int n)
{
	sprintf(num,"%d",n);
	int len=strlen(num);
	for(int i=0;i<=len/2;++i)
	{
		if(num[i]!=num[len-i-1])
			return 0;
	}
	return 1;
}

int main()
{
	int t;
	fin>>t;
	int index;
	for(index=1;index<=t;++index)
	{
		int a,b;
		fin>>a>>b;
		int count=0;
		for(int i=a;i<=b;++i)
		{
			if(isP(i))
			{
				double x=sqrt((double)i);
				int y=(int)x;
				if(x-y==0)
				{
					if(isP(y))
						count++;
				}
			}
		}
		fout<<"Case #"<<index<<": ";
		fout<<count<<endl;
	}
	return 0;
}



