#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

main()
{
	long long int t,i,j,count,sum,len;
	char ip[1001];
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("codejam_q2.out");
	in>>t;
	for(i=1;i<=t;i++)
	{
		in>>ip;
		j=0;
		len=strlen(ip);
		count=0;
		if(len==1)
		{
			if(ip[0]=='+')
				count=0;
			else
				count=1;
		}
		else
		{
			j=1;
			while(j<len)
			{
				if(ip[j]!=ip[j-1])
				{
					count++;
				}
				j++;
			}
			if(ip[len-1]=='-')
			{
				count++;
			}
		}
		out<<"Case #"<<i<<": "<<count<<endl;
	}
	in.close();
	out.close();
}
