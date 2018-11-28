#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<fstream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(7);
	int t;
	double c,f,x;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cin>>c>>f>>x;
		double v=2.0,res=0,before=x/v;
		int i=0;

		while(1)
		{
			res+=c/v;
			v+=f;
			if((res+x/v) > before)
				break;
			before=(res+x/v);
			
		}

		cout<<"Case #"<<tc<<": "<<before<<endl;
	}
	return 0;
}



