#include <bits/stdc++.h>
#define ll long long int
#define ld long double
using namespace std;
int main()
{
	ll t,i;
	ld c,f,x,r,t_tot;
	cin>>t;
	cout<<fixed;
	cout<<setprecision(7);
	for(i=1; i<=t; i++)
	{
		cin>>c>>f>>x;
		//cout<<c<<" "<<f<<" "<<x<<"\n";
		r=2;
		t_tot=0;
		while( ((c/r)+(x/(r+f))) <(x/r))
		{
			t_tot+=c/r;
			r+=f;
			//cout<<i<<"Haha\n";
		}
		t_tot+=x/r;
		cout<<"Case #"<<i<<": "<<t_tot<<"\n";
	}
	return 0;
}