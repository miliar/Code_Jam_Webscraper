#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double r=2;
		double tt=0;
		while(r<(f*(x-c))/c)
		{
			tt+=c/r;
			r+=f;
		}
		tt+=x/r;
		cout<<"Case #"<<i<<": ";
		printf("%0.7lf",tt);
		cout<<endl;
	}
	return 0;
}
