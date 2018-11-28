#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <cmath>
using namespace std;

ifstream cin("B-small-attempt0.in");
ofstream cout("out.txt");

int main()
{
	int t,count=0;
	double c,f,x,now;
	double p1,p2,ans;
	cin>>t;
	while (t--)
	{
		count++;
		cout<<"Case #"<<count<<": ";
		ans=0;
		now=2.0;
		cin>>c>>f>>x;
		while (true)
		{
			p1=x/now;
			p2=c/now+x/(now+f);
			if (p1<p2 || abs(p1-p2)<1e-7)
			{
				ans+=p1;
				break;
			}
			else
			{
				ans+=c/now;
				now+=f;
			}
		}
		cout<<fixed<<setprecision(7)<<ans<<endl;
	}
	return 0;
}