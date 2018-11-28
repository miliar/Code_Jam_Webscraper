//Template
//C++ 4.8.2
#include <iostream>
#include <cstdio>
#include <cmath>
#include <iomanip>
using namespace std;
int main() 
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	int test,m,i,j;
	double c,x,f,t;
	cin>>test;
	for(j=1;j<=test;j++)
	{
		cin>>c>>f>>x;
		if(x<=c)
			m=0;
		else
				m=ceil( (x/c)-1-(2/f) );
		for(t=0,i=0;i<m;i++)
			t+=c/(2+i*f);
		t+=x/(2+m*f);
		cout<<setprecision(10)<<"Case #"<<j<<": "<<t+0.0000000001<<"\n";
	}
	return 0;
}
