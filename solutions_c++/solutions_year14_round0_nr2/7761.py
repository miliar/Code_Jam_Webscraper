#include <iostream>
#include <cstdio>
using namespace std;
 
int main() {
 
 
 
	int t,tc=1;
	cin>>t;
	while(t--)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double co=0.0,val=2.0,ans =0.0,fl=1.0;
		while(fl)
		{
			if(x/val<((c/val)+(x/(val+f))))
			{
				ans+=x/val;
				fl=0.0;
			}
			else
			{
				ans+=(c/val);
				val+=f;
			}
		}
 
 
	printf("Case #%d: %.7f\n",tc++,ans);
		
	}
	return 0;
}

