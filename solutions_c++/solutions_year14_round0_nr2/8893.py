#include <iostream>
using namespace std;
#include<stdio.h>


int n,l;
double rate,c,f,x,t;
int main() {
	// your code goes here
	string fname = "B-large";
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);
	cin>>n;
	while(l<n)
	{
		t=0;
		rate=2;
		cin>>c>>f>>x;
		while((c/rate)+x/(rate+f)<(x/rate))
		{
			t=t+(c/rate);
			rate=rate+f;
		}
		t=t+(x/rate);
		cout.precision(12);
		if(l!=n-1)
		cout<<"Case #"<<l+1<<": "<<t<<"\n";
		else
		cout<<"Case #"<<l+1<<": "<<t;
	l++;

	}
	return 0;
}
