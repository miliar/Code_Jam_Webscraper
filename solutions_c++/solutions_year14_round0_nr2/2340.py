#include <stdio.h>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>


#define TASK   "B-large"


using namespace std;

void solve(){

	double production=2;
	double C = 0;
	double F = 0;
	double X=0;
	
	double a1=0;
	double b1=0;
	double c1=0;

	double b=0;
	
	double result = 0;
	
	scanf("%lf",&C);
	scanf("%lf",&F);
	scanf("%lf",&X);
	
	while(true){
		
		a1 = X/production;
		b1 = X/(production + F);
		c1 = C/production;

		b = b1 + c1;
		
		if(a1 < b){
			result = result + a1;
			break;
		}
		else{
			result = result + c1;
			production = production + F;
		}
	}

		printf("%.7f\n",result);
	
}



int main(int argc, char **argv)
{
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
		
	char buf[1000];
	int testNum;
	gets(buf);
	sscanf(buf,"%d",&testNum);

	for (int testId = 1; testId <= testNum; testId++){
		
		printf("Case #%d: ",testId);
		solve();
		
	}	
	
	return 0;
}
