//============================================================================
// Name        : problem1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int test_cases,s_map[1000][100],i,j,t,k,sum,f;
	int s_max[10010];
	char s_map1[10000];

	cin>>test_cases;
	for(j=0;j<test_cases;j++)
	{


		cin>>s_max[j];
		cin>>s_map1;
		for(i=0;i<s_max[j]+1;i++)
		{
			s_map[j][i]=(int)s_map1[i]-48;
		}
	}
	for(j=0;j<test_cases;j++)
	{
		sum=s_map[j][0];f=0;t=0;

			for(i=1;i<s_max[j]+1;i++)
			{



				if(sum<i)
				{
					f=f+(i-sum);
					t=i-sum;
				}sum=sum+s_map[j][i]+t;t=0;
			}
			cout<<"Case #"<<j+1<<": "<<f<<endl;




	}
	return 0;
}
