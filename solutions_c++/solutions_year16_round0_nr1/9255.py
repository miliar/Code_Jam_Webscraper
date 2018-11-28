#include<fstream.h>
using namespace std;
int main()
{
	long n;
	long x=0;
	ifstream f("A-large.in");
	ofstream g("A-large.out");
	f>>n;
	long j;
	long d[10];
	long cod=0;
	long c,y,s,z=0;
	for(long i=1; i<=n; i++)
	{
		for (j=1; j<=10; j++)
			d[j]=0;
		f>>x;
		y=0;
		if (x==0)
			if(i==1)
			g<<"Case #"<<i<<": "<<"INSOMNIA";
			else
				g<<"\n"<<"Case #"<<i<<": "<<"INSOMNIA";
		else
		{
		cod=0;
		while(cod==0)
		{
			y=y+x;
			z=y;
			while(z>0)
			{
				c=z%10;
				d[c+1]=1;
				z=z/10;
			}
			s=0;
			for(long k=1; k<=10; k++)
				s=s+d[k];
			if(s==10)
			{
				cod=1;
				if(i==1)
				g<<"Case #"<<i<<": "<<y;
				else
					g<<"\n"<<"Case #"<<i<<": "<<y;
			}
		}
		}
		}
	f.close();
	g.close();
return 0;
}