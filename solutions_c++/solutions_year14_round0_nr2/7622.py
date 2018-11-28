#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

ofstream myout;
ifstream myin;

class jar
{
	double C,F,X;

	public:
		jar();
		void output(int);
};

jar::jar()
{
	myin>>C;
	myin>>F;
	myin>>X;
}

void jar::output(int x)
{
	double t=0,a,b,p=2;

	myout<<"Case #"<<x<<": ";
	while(1)
	{
		a=(X/p)+t;
		t=(C/p)+t;
		p=p+F;
		b=(X/p)+t;

		if(b>=a)
		{
			break;
		}
	}

	myout<<setprecision(8)<<a<<endl;
}

main()
{
	int n,i;
	jar *p;

	myin.open("B-large (1).in");
	myout.open("abhie100.txt");

	myin>>n;
	p=new jar[n];

	for(i=0;i<n;i++)
	{
		p[i].output(i+1);
	}

	return 0;
}
