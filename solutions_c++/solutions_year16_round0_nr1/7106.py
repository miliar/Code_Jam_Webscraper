#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	long long int n,t,i,j,c,p,m,x;
	int a[10]={0};
	ofstream myfile;
	myfile.open("Output.txt");
	
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		c=0;
		p=1;
		for(j=0;j<10;j++)
		a[j]=0;
		if(n==0)
		myfile<<"Case #"<<i<<": INSOMNIA\n";
		else
		{
		while(c<=10)
		{
			m=p*n;
			x=m;
			while(m>0)
			{
				a[m%10]=1;
				m=m/10;
			}
			for(j=0;j<10;j++)
			c=c+a[j];
			if(c==10)
			{
				myfile<<"Case #"<<i<<": "<<x<<"\n";
				break;
			}
			c=0;
			p++;
		}
	}
}
myfile.close();
return 0;
}

