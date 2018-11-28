#include <cstdio>
#include <iostream>
using namespace std;
int main() {
    int T;
    double C, F, X;
    cin>>T;
    for(int caso=1 ; caso<=T; caso++) {
    	cin>>C>>F>>X;
    	double seg = 0.0, inc = 2.0, segDirecto, segGranja;
    	while(true) {
    		segDirecto = X/inc;
    		segGranja = C/inc + X/(inc + F);
   			//cout<<segDirecto<<" "<<segGranja<<endl;
    		if(segDirecto > segGranja){
    			seg += C/inc;
    			inc += F;
    		}
    		else {
    			seg += segDirecto;
    			break;
    		}
    	}
    	printf("Case #%d: %.7lf\n", caso, seg);
    }
    return 0;
}