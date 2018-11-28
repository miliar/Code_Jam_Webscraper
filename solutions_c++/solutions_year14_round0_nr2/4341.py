#include<iostream>
#include<cstdio>
#include <cstring>

using namespace std; 

int main () {
	 int T;
        cin>>T;
	double out[T];
	double base = 2;
	double rate, farm, limit;
	double total=0;
	for (int i =0; i < T; i++){
		base=2;
		total=0;
		scanf("%lf%lf%lf", &farm, &rate, &limit);
		while (true){
			if (limit/base < farm/base + limit/(base+rate ) ){
				
				out[i]= total+limit/base;
				break;
			}else {
				
				total+=farm/base;
				base+=rate;
			}
		}
	}
	for (int i =0; i < T; i++){
		printf ("Case #%d: %.7lf\n",i+1,out[i] );
	}
}
