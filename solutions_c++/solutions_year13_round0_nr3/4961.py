#include <iostream>
#include<math.h>
#include<fstream>
using namespace std;

	int swap(int a)
{
	int y=0;
	int r,m;
	r=a;
	for(;a!=0;)
	{
		m=a%10;
		y=y*10+m;
		a=a/10;
	}
	if(y==r)
		return 1;
	else
		return 0;
}

int main ()
{
	ifstream in ("C-small-attempt0.in");
	ofstream out ("outputt.txt");
	long min,max;
	int n;
	in>>n;
	double q ;
	for (int j=0;j<n;j++)
{
	in>>min;
	in>>max;

	int count=0;
	for (long i=min;i<=max;i++)
	{
		if (swap(i))
		{
			q=sqrt(i);
			
			if (q==(int)q)
			{	if( swap(q))
					count++;
			}
		}
	}
	out<<"Case #"<<j+1<<": "<<count<<endl;
	
}
}
