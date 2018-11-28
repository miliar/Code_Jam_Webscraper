//#include <simplecpp>
#include<iostream>
#include<string>
#include<fstream>

using namespace std;


int main(int argc, char* argv[ ]) {
	long int T, n;
	double c, f, x, nt, answer, term;
	cin>>T;
	cout.precision(7);
	for (int t=1; t<=T; t++) {
		cin>>c>>f>>x;
		nt=(x*f-2.0*c)/(c*f);
		//cout<<nt;
		n=nt;
		//cout<<"   "<<n;
		answer=0;
		if (nt>0) {
			for (long int r=0; r<n; r++) {
				term=c/(2.0+r*f);
				answer+=term;
				//cout<<"*"; //
			}
			answer+=x/(2.0+n*f);
		}
		else answer=x/2.0;
		cout<<"Case #"<<t<<": "<<fixed<<answer<<endl;
	}
}