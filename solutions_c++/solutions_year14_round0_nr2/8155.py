#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int a[4][4];
int b[4][4];
int cuenta[17];

int main(){
	int tc;	
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		double C,F,X;
		double cant=2;
		cin>>C>>F>>X;
		double mini=X/2.0;
		double t=0;
		
		while(t<mini){
			mini=min(mini,t+ X/cant );
			t+=C/cant;
			cant+=F;
		}
		
		printf("%.10lf\n",mini);
	}
	
	return 0;
}

