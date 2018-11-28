#include <iostream>
#include <string>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <list>
using namespace std;

#define ll long long
#define ull unsigned long long
#define INF 1e9

int main(){
	ios_base::sync_with_stdio(0);

	int t;
	double c,f,x,total,tt,rate;
	cin>>t;
	for(int k = 1; k<=t;k++){
		cin>>c>>f>>x;
		total = 0;
		tt=0;
		rate = 2;
		while(1){
			double tReq = (x)/rate;
			double tNew = c/rate + x/(rate+f);
			if(tNew < tReq){
				tt = tt + c/rate;
				rate = rate+f;
			}else{
				tt = tt + x/rate;
				break;
			}
		}
		printf("Case #%d: %.7f\n",k,tt);
	}

	return 0;
}
