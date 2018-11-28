// Author:S Giritheja
//Program to evaluate number of friends required to provide standing ovation to the presenter.
#include <iostream>
#include <string.h>
using namespace std;
int main () {
	int t,x=0; //testcases
	cin>>t;
	while(t--) {
		int smax;
		cin>> smax;
		char audience[smax+1];
		cin>>audience;
		int present = (int)audience[0]-48;//audience present to give standing ovation
		int required = 0;//audience required to give standing ovation
		for(int i=1;i<smax+1;i++) {
			int value=(int)audience[i]-48;//converting char to actual value.
			if( present >=i || value==0 ) {
				present+=value;
			} else {  
				required+=(i-present);
				present=i+value;
				
			}
		
		}
		cout<<"Case #"<<++x<<": "<<required<<endl;
	}
	
	return 0;
}