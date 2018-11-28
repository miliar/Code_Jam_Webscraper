#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	int T; cin>>T;
	cout.precision(7);
	for(int i=0;i<T;++i){
		double C,F,X;
		cin>>C>>F>>X;
		int m=0;
		double tm=X/2,t;

		while((X-C)/(2+m*F)> X/(2+(m+1)*F)){
		t=X/(2+m*F);
		for(int j=0;j<m;++j){
			t+=C/(2+j*F);
		}

	++m; if(t<tm){tm=t;}
		} t=X/(2+m*F);
		for(int j=0;j<m;++j){
			t+=C/(2+j*F);
		}if(t<tm){tm=t;}

		cout<<"Case #"<<i+1<<": "<<fixed<<tm<<endl;
	}

}

