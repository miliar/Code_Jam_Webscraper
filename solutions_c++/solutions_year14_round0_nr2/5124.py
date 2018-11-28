#include <iostream>
# include <string>
# include <iomanip>
# include <stdio.h>
using namespace std;
int main()
{
	freopen("CODEJAM_Q2.txt","w",stdout);
	int t;
	cin>>t;
	for (int x=1;x<=t;x++)
	{
		long double c,f,goal;
		cin>>c>>f>>goal;
		long double mi=goal/2.0;
		long double before=0;
		long double g=2;
		while (true)
		{
			long double now=before+c/g+goal/(g+f);
			if (now>mi)
				break;
			mi=now;
			before=before+c/g;
			g=g+f;
		}
		cout<<"Case #"<<x<<": "<<setprecision(7)<<fixed<<mi<<endl;
	}
}