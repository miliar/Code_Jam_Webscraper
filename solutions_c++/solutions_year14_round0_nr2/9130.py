#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;
//#define SMALL
#define LARGE

int main(){
    int T;
    double C,F,X;
#ifdef LARGE    
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
#endif    

    cin >> T;
    for(int cur = 1; cur<= T; cur++){
        cin >> C;
        cin >> F;
        cin >> X;
        double time=0.0;
        double div=2.0;
        bool WW=true;
        double D,sum1,sum2;
			while(WW){	
				sum1=time+X/div;
				time+=C/div;
				div+=F;
				D=X/div;
				sum2=time+D;
				if(sum1<sum2)
					WW=false;
			}
		printf("Case #%d: %.7f\n", cur, sum1);
    }
	
    return 0;
}

