#include<iostream>
#include<stdio.h>
#include<string>
#include<algorithm>
#include<vector>


using namespace std;


int main(){
	freopen("b.txt","r",stdin);
	int T; cin>>T;
	for(int cn=1;cn<=T;cn++){
		double c,f,x; cin>>c>>f>>x;
		double prev = x/2.0;
		double time = 0.0;
		for(int i=0;;i++){
			time+=(c/(i*f+2.0));
			double tmp = x / ((i+1)*f+2.0);
			tmp+= time;
			if(tmp < prev){
				prev = tmp;
			}else break;
		}
		cout << "Case #"<<cn<<": ";	
		printf("%.7f\n",prev);
	}
	return 0;
}
