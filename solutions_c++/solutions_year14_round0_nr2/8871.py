#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <string>

#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define pii pair<int, int>
#define pn(n) printf("%d\n",n)
#define sn(n) scanf("%d",&n)
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)

#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i,a,b) for(i = a; i <= b; i++)
	
typedef long long int li;
using namespace std;

int main(){
	int test;
	sn(test);
	int no=0;
	while(test--){
		no++;
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double addedCost=0.0;
		double minTime=x/2.0;
		double numForward=1.0;
		double newMinTime=0.0;
		while(1){
			//printf("%lf\n",minTime);
			addedCost=addedCost+c/(2.0+(numForward-1)*f);
			newMinTime = ( x/(2.0+numForward*f) + addedCost );
			numForward++;
			if(newMinTime<=minTime){
				minTime=newMinTime;
			}
			else{
				break;
			}
		}
		printf("Case #%d: %.7lf\n",no,minTime);
	}
	return 0;
}

