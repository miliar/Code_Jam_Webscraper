#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (){
	int t;
	cin >>t;
	for (int u = 0; u < t; u++){
		double c,f,x;
		cin >>c>>f>>x;
		double cookies = 2.;
		double time = 0.;
		while (x/cookies > c/cookies + x/(cookies+f)){
		
			//cout <<x/cookies<<" "<<c/cookies + x/(cookies+f)<<endl;
			time+=	c/cookies;
			cookies+=f;
		} 
		time+=x/cookies;
		cout.precision(7);
		cout <<"Case #"<<u+1<<": "<<fixed<<time<<endl; 
	}

}