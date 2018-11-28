#include <iostream>
using namespace std;

int main() {
	int t,q,i;
	double c,x,f,s,d,m;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>c>>f>>x;
		d=2.0;
		s=0.0;
		q=(int)x/c;
		
		if(q==0)
		{
			m=x/d;
		}
		while(q>0)
		{
			
			m=s+x/d;
			s+=c/d;
			
			d+=f;
			if(m<s+x/d)
				break;
			
			
		}

		printf("Case #%d: %.7f\n",i,m);
	}
	return 0;
}