
#include "stdafx.h"
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream> 

using namespace std;
int main()
{
	std::ofstream ofs ("out.txt", std::ofstream::out);

	int t;

	cin>>t;
	for(int q=1;q<=t;q++)
	{
		int a,b,k;
		cin>>a>>b>>k;
		a=a-1;
		b=b-1;
		k=k-1;

		int min = (a>b?b:a);
		int max = (a<b?b:a);
		//what if equ
		int cnt =0;// = (k+1)*(k+1);
		//if(k==0)
		//{
		//	ofs<<"Case #"<<q<<": "<<"1"<<"\n";
		//	continue;
		//}
		//if(k >= min)
		//{
		//	ofs<<"Case #"<<q<<": "<<(a+1)*(b+1)<<"\n";
		//	continue;
		//}
		//else
		//{
			for(int i=0 ; i<=max; i++)
			{
				for(int j=min ; j>=0;j--)
				{
					if((i&j) <= k)
					{
						cnt++;
					}
				}
			}
			ofs<<"Case #"<<q<<": "<<cnt<<"\n";
		//}
	}
	ofs.close();
	return 0;
}
