#include <stdlib.h>
#include <fstream>
using namespace std;

int main ()
{
	ifstream R("a2.in");
    ofstream W("a2.out");
    
    int t;
    R>>t;
    for (int ti=1;ti<=t;++ti)
    {
		long long r,p;
		R>>r>>p;
		long long ii=0,ans=0;
		while (p>0)
		{
			p=p-1-2*r-4*ii;
			ii=ii+1;
			if(p>=0)
				ans++;
		}
		W<<"Case #"<<ti<<": "<<ans<<endl;
	}
}
