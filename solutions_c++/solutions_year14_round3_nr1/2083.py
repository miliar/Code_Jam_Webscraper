//============================================================================
// Name        : r1_3prblm1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
#include <strings.h>
using namespace std;

int main()
{
	string *str;
	int t,*ans,z;
	//cout<<"Enter the number of test cases:";
	cin>>t;
	long long int p=0,q=0,rem=0,div=0,temp1=0,temp2=0;
	ans=new int[t];
	str=new string[t];
	//cout<<"Enter the p&q:";
	for(z=0;z<t;z++)
	{
		p=0;q=0;rem=0;div=0;temp1=0;temp2=0;
		cin>>str[z];


		int i=0;
		while(str[z][i]!='/')
		{
			p*=10;
			p+=(int(str[z][i])-48);
			i++;
		}
		i++;
		while(i!=(str[z].length()))
		{
			q*=10;
			q+=(int(str[z][i])-48);
			i++;
		}

		temp1=p;
		temp2=q;


		if(q%p==0)
		{
			q/=p;
		}
		int count=0;
		while(rem==0&&q!=0&&count<42)
		{
			count++;
			rem=q%2;
			q/=2;
		}
		if(q==0)
		{
			count=0;
			while(temp1<temp2)
			{
				temp1*=2;
				count++;
			}
			ans[z]=count;

		}
		else
		{
			ans[z]=-1;
		}
	}

	for(z=0;z<t;z++)
	{
		if(ans[z]!=-1)
		{
			cout<<"case #"<<(z+1)<<": "<<ans[z]<<endl;
		}
		else
		{
			cout<<"case #"<<(z+1)<<": impossible"<<endl;
		}
	}

	return 0;
}
