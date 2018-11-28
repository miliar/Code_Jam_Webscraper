#include <iostream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <math.h>
#include <limits.h>
#include <time.h>
#include <vector>
#include <utility>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define LIM_UI UINT_MAX
#define LIM_UL ULLONG_MAX
//iterations
#define repi(i,a,b) for(int i=a;i<=b;++i)
#define repd(i,a,b) for(int i=a;i>=b;--i)

int main(){
	ios::sync_with_stdio(false);
	int t;
	double c,f,x;
	cin>>t;
	int cs = 1;
	while(cs<=t){
		cin>>c>>f>>x;
		double rate = 2.0;
		double tempt = c/2,ftime = x/2;
		while(true){
			rate+=f;
			double newtime = tempt+x/rate;
			if(newtime>ftime)
				break;
			else{
				ftime = newtime;
				tempt+= c/rate;
			}
		}
		printf("Case #%d: %.7lf\n",cs,ftime);
		++cs;
	}
	return 0;
}