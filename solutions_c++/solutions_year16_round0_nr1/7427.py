#include<iostream>
using namespace std;

int a[10];
int check()
{
	for(int i=0;i<10;i++)
	{
	if(a[i]==0)
	return 0;
}
	return 1;
}
void reset()
{
for(int i=0;i<10;i++)
	a[i]=0;	
}
void calculate(int p)
{
int q;int c=0;
		while(p>0)
		{
			q=p%10;
			
			a[q]=1;
			p=p/10;
		
		}		
}
int main()
{
	int t,i,n,j,m,s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		if(n==0)
		cout<<"Case #"<<i<<": "<<"INSOMNIA\n";
		else
		{
		reset();
	    s=check();
	    int c=n;
	    while(s!=1)
	    {
	    	calculate(n);
	    	n=n+c;
	    	s=check();
	    }
		cout<<"Case #"<<i<<": "<<n-c<<endl;
		}
	}
}