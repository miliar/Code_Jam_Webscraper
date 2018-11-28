#include <iostream>
#include<cstdio>
using namespace std;

int main() {
    freopen("a.in","r",stdin);
    freopen("bit2.out","w",stdout);
	int t,jk;
	double c,f,x,t1,n,c1;
	cin>>t;
	for(jk=1;jk<=t;jk++)
	{
		t1=0;
		n=2;
		cin>>c>>f>>x;
		
		c1=0;
		
		while(c1<=x)
		{
			if((x-c)/(double)n<x/(n+f))
			{
				t1+=x/n;
				break;
			}
			else
			{
				t1+=c/n;
				n+=f;
			}
			//cout<<"done"<<endl;
		}
		printf("Case #%d: %.7lf\n",jk,t1);
	}
	// your code goes here
	return 0;
}
