#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
long long no[1000000];

int main()
{
	ifstream rf("input.txt");
	ofstream wf("result.txt");
	long long int t,a,b,p,res,x,y;
	rf>>t;
	for(int i=1;i<=t;i++)
	{
		res=0;
		y=0;
		rf>>a>>b;
		x=a;
		p=a*a;
		while(res<=b)
		{
			res+=(2*x+1);
			y++;
			x+=2;
		}
		wf<<"Case #"<<i<<": "<<y-1<<"\n";
	}
	
	return 0;
}
