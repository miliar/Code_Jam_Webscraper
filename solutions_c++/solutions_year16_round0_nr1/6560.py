#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ofstream out("A-large.txt");
	long long int n,s=0,t=0,m=0,r=0,test;
	int a[9]={0,0,0,0,0,0,0,0,0};
	cin>>test;
	for(int k=0;k<test;k++)
	{
	cin>> n;
	for(int i=1;i<100000;i++)
	{
		s = i*n;
		t=s;
		for(int j=0;t!=0;)
		{
			m=t%10;
			a[m]=1;
			if(a[0] && a[1] && a[2] && a[3] && a[4] && a[5] && a[6] && a[7] && a[8] && a[9] )
			{
				r=n*i;
				break;
			}
			t/=10;
			
		}
		if(r!=0)
		 break;
	}
	if(r!=0)
	out<<"Case #"<<k+1<<": "<<r<<"\n";
	else
	out<<"Case #"<<k+1<<": INSOMNIA"<<"\n";
	for(int h=0;h<10;h++)
	a[h]=0;
	r=0;
	}
}
