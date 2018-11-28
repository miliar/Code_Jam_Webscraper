#include<fstream.h>
#include<string>
#include<iostream.h>
using namespace std;
int main()
{
	ifstream f("B-large.in");
	ofstream g("B-large.out");
	char z[101];
	int v[101];
	int n,l;
	f>>n;
	f.get();
	int i,s,x,m,y,k,nr;
	for(i=1; i<=n; i++)
	{
	f.getline(z,101);
	l=strlen(z);
	
	for(int j=0; j<l; j++)
		{if(z[j]=='-')
			v[j+1]=0; 
		else
			v[j+1]=1;
		}
	s=0;
	for(k=1; k<=l; k++)
		s=s+v[k];
	nr=0;
		for (m=1; m<=l-1&&s!=l; m++)
		{
			if(v[m]!=v[m+1])
			{
				for(int n=1; n<=m; n++)
				if(v[n]==0) v[n]=1; else v[n]=0;
				
			nr++;
			s=0;
			for(k=1; k<=l; k++)
				s=s+v[k];
			}
		}
		if(s!=l)
			nr++;
		if(i!=1)
		g<<"\n"<<"Case #"<<i<<": "<<nr;
		else
			g<<"Case #"<<i<<": "<<nr;
	}
	f.close();
	g.close();
	return 0;
}