#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int t;
	cin>>t;
	for(int p = 0; p < t; p++){
		double c, f ,x;
		cin>>c>>f>>x;
		double prod = 2;
		double dur = 0;
		while(true){
			double tofac = c / prod;
			double without = x / prod;
			if(without < tofac + (x / (prod + f))){
				dur += without;
				break;
			}
			else{
				dur += tofac;
				prod += f;
			}
		}
		cout<<"Case #"<<p + 1<<": ";
		printf("%.7lf\n", dur);
	}
	return 0;
}