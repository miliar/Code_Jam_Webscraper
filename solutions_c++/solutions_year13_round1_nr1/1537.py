#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<new>
#include<iomanip>
#include<fstream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
using namespace std;
char str[300],ch;
int main()
{
	long long int sum,count=0,k,i=1,t,flag=0,r,mi;
	char ch,s;
	//cout<<sizeof(a)<<i;
	//scanf("%d",&t);
	ifstream p("p.txt");
	ofstream o("pra.txt");
	p>>t;
	//p.get(ch);
	for(k=1;k<=t;k++)
	{
		count=0;sum=0;
		p>>r>>mi;
		i=1;
		while(1)
		{
			//cout<<"sum:"<<sum<<endl;
			sum=sum+2*(r+i)-1;
			if(sum<=mi) count++;
			else break;
			i+=2;
		}
		//p.getline(str,300);
		o<<"Case #"<<k<<": "<<count<<endl;
	}
	p.close();
	o.close();
	return 0;
}
