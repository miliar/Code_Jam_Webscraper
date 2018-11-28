/* 
 * Author: Mohamad Shawkey
 * Created on April 12, 2014, 2:59 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;


int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	
	for(int i=1;i<=t;i++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double ot,of,nt,ores,nres;
		int it=0;
		ot=0.0;
		ores=x/2.0;
		while(true)
		{
			of=2.0+f*it;
			nt=ot+c/of;
			nres=nt+x/(of+f);
			if(ores<nres) break;
			else {ores=nres; ot=nt; it++;}
		}
		cout<<"Case #"<<i<<": ";
		printf("%.7f\n",ores);
	}
	return 0;
}

