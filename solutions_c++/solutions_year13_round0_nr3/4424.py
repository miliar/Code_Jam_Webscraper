#include <iostream>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <fstream>
using namespace std;
long long t;
long long n,m;
bool check(long long mm)
{ 
	char chi[10];
   string s;
   long long nn;
   bool flag=true;
   int m,i;
   nn=mm;
   ltoa(nn,chi,10);
   s=chi;
   for(i=0;i<=s.length()/2-1;i++)
     if(s[i]!=s[s.length()-i-1])
     {flag=false;
        break;
     }
   if ((flag)||s.length()==1)  
      return 1;
      return 0;
} 



int main()
{
	long long i,j;
	long long ans;
	long long tem;
	ifstream icin;
	icin.open("C-small-attempt4.in");
	ofstream ocout;
	ocout.open("gg3.out");
	icin>>t;
	for (i=1;i<=t;i++)
	{
		ans=0;
		icin>>n>>m;
		for (j=n;j<=m;j++)
		{
			tem=floor(sqrt(j));
			if(tem*tem==j)
			{
				if ((check(j)==1)&&(check(tem)==1))ans++;
			}
		}	
		ocout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}

