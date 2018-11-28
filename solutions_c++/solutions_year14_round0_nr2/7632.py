#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<PII> VPII;

typedef vector<double> VD;
typedef vector<string> VS;

typedef long long LL;

int main(){ 	
	int cases;
	scanf("%d\n", &cases);
	
	for(int caseNr = 1; caseNr <= cases; caseNr++){
	  // INIT
	  double C, F, X;
	  
	  // READ
	  scanf("%lf %lf %lf\n", &C, &F, &X);	  
	  
	  // PROCESS
	  double sum = 0.0;
	  double rate = 2.0;
	  double time = 0.0;
	  while(sum < X){
	    //printf("time=%lf, sum=%lf, rate=%lf\n", time, sum, rate);
	    double skip;
	    
	    double timeToEnd = (X - sum) / rate;
	    double timeToEndWithFarm = (X - (sum - C)) / (rate + F);
	    
	    if(sum < C){
	      // we cannot buy a farm -> wait until we can buy a farm
	      skip = (C - sum) / rate;
	    }else{
	      // we can possibly buy a farm
	      if(timeToEndWithFarm < timeToEnd){
	        // buy it
	        sum -= C;
	        rate += F;
	        continue;
	      }else{
	        // better do not buy it
	        skip = timeToEnd;
	      }
	    }
	    skip = min(timeToEnd, skip);
	    skip = max(skip, 0.00000001);
	    sum += rate * skip;
	    time += skip;
	  }
	  
	  // OUTPUT
		printf("Case #%d: %.7lf", caseNr, time);
		
		printf("\n");
		fflush(stdout);
	}
	
	return 0;
}
