// Craciun Catalin
//  B
//   Google Code Jam
#include <iostream>
#include <iomanip>

using namespace std;

int t;
double c, f, x, r=2.0;

void solve()
{
	r=2.0;
	
	double time=x/r;
	double newTime=0;
	
	for (int i=1;i<=20000;i++)
	{
		newTime=newTime+c/r;
		r=r+f;
		
		if (newTime+x/r<time)
			time=newTime+x/r;
	}
	
	cout<<fixed<<setprecision(7)<<time;
}

int main()
{
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>c>>f>>x;
		cout<<"Case #"<<i<<": ";
		solve();	
		cout<<'\n';
	}
	
	return 0;
}
