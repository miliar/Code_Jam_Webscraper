#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin>>T;
	int k=0;
	while(T--)
	{
		if(k)
		cout<<endl;
		k++;
		cout<<"Case #"<<k<<": ";
		double c,f,x;
		cin>>c>>f>>x;
		double temp=c/2.0;
		double res=x/2.0;
		double init=2.0+f;
		int j=0;		
		while(j<100001)
		{
			j++;
			res=min(res,temp+(x/init));
			temp=temp+(c/init);
			init=init+f;	
		}
		printf("%.7lf",res);
		
	}
}
