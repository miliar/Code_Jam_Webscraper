#include <fstream>
#include <iostream>
#include<iomanip>

using namespace std;


double c,f,x,tot,now,ans,i;
int t,tt;

ifstream fin("B-large.in");
FILE* fout;


int main()
{
	fout=fopen("B.txt","w");
	fin>>t;
	for(tt=1;tt<=t;tt++)
	{
		fin>>c>>f>>x;
		tot=0.0;
		now=2.0;
		ans=100000.0;
		for(i=0;i<100000;i++)
		{
			if (ans>tot+x/now)
				ans=tot+x/now;
			tot=tot+c/now;
			now=now+f;
		}
		if (ans>tot+x/now)
			ans=tot+x/now;		
		fprintf(fout,"Case #%d: %.7f\n",tt,ans);
	}
	return 0;
}