#include<iostream>
using namespace std;
class m
{
	public:
	int n;int s[10];
	int e,i,c,z,n1;
	void e1()
	{
		cin>>e;
		for(i=0;i<10;i++)
		s[i]=10;
		c=0;
		for(i=1;i<=e;i++){
		in();
		c=0;}
	}
	void in()
	{int j;
		cin>>n;n1=n;
		for(j=0;j<10;j++)
		s[j]=10;
		if(n==0)cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
		s1();
	}
	void d()
	{	int j;
		for(j=0;j<10;j++)
		{
			
			if(s[j]!=j)
			{
				z=0;
				break;
			}
			else z=1;
		}
		if(z==1)
		cout<<"Case #"<<i<<": "<<n1<<endl;
		else if(z==0)
		{ c++; n1=n*c;  s1();};
		if(n==0)cout<<"Case #"<<i<<"Insomania"<<endl;
	}
	void s1()
	{
		int d1;
		int l;		l=n1;
		while(l!=0)
		{
			d1=l%10;
			l=l/10;
			s[d1]=d1;
		}d();
	}
	
};
main()
{
	m t1;
	t1.e1();
}
