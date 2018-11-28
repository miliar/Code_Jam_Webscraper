#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include <vector>
using namespace std;

int main() {
	cout<<fixed<<setprecision(7);
	int n=0;
	cin>>n;
	for(int i=1; i <= n; ++i){
		double C=0,F=0,X=0,t1=1,t2=0,t=0,k=0;
			cin>>C>>F>>X;
			while(t1>t2){
					t1=X/(k*F+2);
					t2=C/(k*F+2)+X/((k+1)*F+2);
					if (t2<t1){
							t+=C/(k*F+2);
							++k;
					}
			}
			t+=t1;
		cout<<"Case #"<<i<<": "<<t<<endl;				
	}
}