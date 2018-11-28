#include <iostream>
#include<cmath>
#include<iomanip>
#include <fstream>
using namespace std;

int main(void) {
	ifstream cin("B-large.in");
    ofstream cout("humble.out");
    int k;
    cin>>k;
	for(int i=0;i<k;++i){
		double c, f  ,x, n, t=0;
		cin>>c>>f>>x;
        n=x/c-2/f-1;int j=0;
		for(;j<n;++j) t+=c/(2+j*f);
        t+=x/(2+j*f);
		cout<<"Case #"<<i+1 <<": "<<setprecision(12)<<t<<endl;
    }
	return 0;
}
