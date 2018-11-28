#include <cmath>
//#include <iostream>
#include <fstream>
using namespace std;

bool pallindrome(__int64 p)
{
	short a[15]={0},i=0;
	while(p)
	{
		a[i++] = p%10;
		p /= 10;
	}
	for (short j=0;j<i/2;j++)
	{
		if (a[j]!=a[i-j-1])
		{
			return false;
		}
	}
	return true;
}


void main()
{
	__int64 M,N;
	int	C;
	ifstream fin("C-small-attempt0.in",ios_base::in);
	ofstream fout("C-small-attempt0.out",ios_base::out);
	fin>>C;
	for(int c=0;c<C;c++)
	{
		fin>>M>>N;
		__int64 count=0;
		for (__int64 n=M;n<=N;n++)
		{
			double d=sqrt((double)n);
			if (d-floor(d) == 0)
			{
				if (pallindrome((__int64)d) && pallindrome(n))
				{
					++count;
				}
				n += (__int64)(2*d);
			}
		}
		fout<<"Case #"<<c+1<<": "<<count<<endl;
	}
	fin.close();
	fout.close();
	//getchar();
}