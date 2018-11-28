#include <iostream>
using namespace std;

#include <string.h>
#include <stdio.h>
#include <math.h>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <limits>

using namespace std;

int main(){
    int c;
    scanf("%d",&c);
    int casenum = 0;
    while(c--){
    	casenum++;
    	double cc;
    	double ff;
    	double xx;
    	double time = 0;
    	double cooks = 2;
    	scanf("%lf %lf %lf", &cc, &ff, &xx);
    	while(1){
    		if(cc/cooks+xx/(cooks+ff) >= xx/cooks){
    			time += xx/cooks;
    			break;
    		}else{
    			time += cc/cooks;
    			cooks += ff;
    		}
    		
    	}
    	printf("Case #%d: %.7lf\n", casenum, time);
    }

	return 0;
}