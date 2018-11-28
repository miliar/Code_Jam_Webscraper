#include <bits/stdc++.h>
using namespace std;
double EPS = 1e-6;


int main (int argc, char const* argv[])
{
	int t;
	freopen ("cookie1.txt","w",stdout);
	cin>>t;
	for(int i = 0;i < t;++i){
		long double c,f,x,r=2.0,t=0.0;
		cin>>c>>f>>x;
		 while ((x/r) > (c/r) + (x/(r+f))) {
			t = t + (c/r);
			r = r + f;
		}
		t = (x/r) + t;
		cout.precision(7);
		cout<<"Case #"<<i+1<<": "<<fixed<<t<<endl;

	}
	return 0;
}
