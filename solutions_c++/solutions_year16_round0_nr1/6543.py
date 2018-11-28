#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
vector<bool> V;
int cont;
void digits(int n)
{
	while(n>0)
	{
		if(!V[n%10])
		{
			cont++;
			V[n%10]=true;
		}
		n=n/10;
	}
}
int main()
{
	ifstream I("A.in");
	ofstream O("A.out");
	int cp,n,x;
	I>>cp;
	for(int i=1;i<=cp;i++)
	{
		cont=0;
		V.assign(10,false);
		I>>n;
		O<<"Case #"<<i<<": ";
		if(n==0)
		{
			O<<"INSOMNIA"<<endl;
			continue;
		}
		else
		{
			x=1;
			while(cont<10)
			{
				digits(n*x);
				x++;
			}
			x--;
			O<<n*x<<endl;
		}
	}
}
