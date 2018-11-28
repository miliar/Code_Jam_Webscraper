#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <vector>

using namespace std;

int main() {
	
	int tt,n,v;
	double na[1000+10],ke[1000+10];
	cin>>tt;
	
	for(int t = 1;t<=tt;t++){
		printf("Case #%d: ",t);
		double c,f,x;
		cin>>c>>f>>x;
		double k = 2.0;
		double time = 0;
		double noFarm = x/k;
		double wiFarm = c/k + x/(k+f);
		while(noFarm >= wiFarm){
			time += c/k;
			k += f;

			noFarm = x/k;
			wiFarm = c/k + x/(k+f);
		}
		printf("%.7f\n", time + noFarm);
	}
	
	return 0;
}