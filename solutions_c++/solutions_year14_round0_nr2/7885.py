#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
ofstream fileout;
ifstream filein;
class container
{
	double C,F,X;
	public:
		container();
		void output(int);
};
container::container()
{
	filein>>C;
	filein>>F;
	filein>>X;
}

void container::output(int x)
{
	double temp=0,pm,mp,p=2;
	fileout<<"Case #"<<x<<": ";
	while(1)
	{
		pm=(X/p)+temp;
		temp=(C/p)+temp;
		p=p+F;
		mp=(X/p)+temp;	
		if(mp>=pm)
		{
			break;
		}
	}
	fileout<<setprecision(8)<<pm<<fixed<<endl;
}

main()
{
	int n,i;
	container *p;
	filein.open("input.in");
	fileout.open("upload.txt");
	filein>>n;
	p=new container[n];
	
	for(i=0;i<n;i++)
	{
		p[i].output(i+1);
    }	
	return 0;
}
