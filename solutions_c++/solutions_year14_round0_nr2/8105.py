#include<iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main()
{
	int t;
    long double c;
    long double f;
    long double x;
    long double inc;
    long double st;

	freopen("B-large.in","rt",stdin);
	freopen("output.in","wt",stdout);
	cin>>t;
	for(int i= 1;i<=t;i++)
	{
		cin >> c;
		cin >> f;
		cin >> x;
		inc=2.0;
		st=x/inc;
		long double farmt=0.0 ;

		while(true)
		{
		    long double onef=farmt+(c/inc)+(x/(inc+f));
			if (st<onef)
			 {
          		break;
        	 }
			 else
			 {
		          farmt+=c/inc;
		          inc+=f;
		          st=onef;
        	 }
		}
		cout << fixed;
	    cout <<"Case #"<<setprecision(7)<<i<<": "<<st<<endl;

	}
	return 0;
}
