#include<iostream>
#include <cstdio>
using namespace std;

int main (int argc, char *argv[]) {
	int t;
	double c, f, x, tot_time, cr; //cr -> cookie rate
	cin>>t;
	for(int tc=0;tc<t;tc++) { 
		tot_time = 0;
		cr = 2;
		cin>>c>>f>>x;
		while(x/cr > c/cr + x/(cr+f)){
			tot_time += c/cr;
			cr += f;
		}
		tot_time += x/cr;
		
		printf("Case #%d: %0.7f\n", tc+1, tot_time);
	}
	return 0;
}

