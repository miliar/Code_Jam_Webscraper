#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main(int argc, char const *argv[]){
	int T;
	double C,F,X;
	cin >> T;
	for(int cn = 1; cn <= T; cn++){
		cin >> C >> F >> X;
		double cRate = 2;		
		double result = 0;
		while(1){
			if( (X-C)/cRate < X/(cRate+F)){ // direct
				result += X/cRate;
				break;
			}else{ // new farm
				result += C/cRate;
				cRate += F;
			}
		}
		printf("Case #%d: %.7f\n",cn,result);		
	}

	return 0;
}