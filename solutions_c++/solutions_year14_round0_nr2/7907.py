#include <iostream>
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <set>
#include <list>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>
#include <stack>
#include <functional>
#include <math.h>
#include <queue>
#include <vector>
#include <bitset>
#include <cstdio>
#pragma comment(linker, "/STACK:2048000000000000")
typedef long long ll;
#define eps 1e-10
#define MP make_pair
 
using namespace std;

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		double c,f,x,ans,cps,time=0.0,farms=0.0;
		cin>>c>>f>>x;
		cps=2.0;
		ans=x/cps;
		double gold=0.0;
		while (true){
			time=time+c/cps;
			cps+=f;
			double ttime=time+x/cps;
			if (ttime+eps<ans){
				ans=ttime;
			}
			else {
				break;
			}
		}
		cout<<"Case #"<<ii<<": ";
		cout.setf(ios::fixed);
		cout.precision(8);
		cout<<ans<<endl;
	}
}