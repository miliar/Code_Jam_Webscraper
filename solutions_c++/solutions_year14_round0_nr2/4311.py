#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>

#define gc getchar_unlocked

using namespace std;

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int main()
{	
	int T;
	double timeTaken,t1,t2,tr,C,F,X,rate;
	scanint(T);
	for(int t=1;t<(T+1);t++) {
		timeTaken = 0;
		rate = 2;
		scanf("%lf",&C);
		scanf("%lf",&F);
		scanf("%lf",&X);

		t1 = (double)X/rate;
		tr = (double)C/rate;
		t2 =  tr + (double)X/(rate+F);

		while( (t1-t2) >= 0.000000001) {
			timeTaken += tr;
			rate += F;
			t1 = (double)X/rate;
			tr = (double)C/rate;
			t2 =  tr + (double)X/(rate+F);
		}

		timeTaken = timeTaken + t1;
		printf("Case #%d: %.7f\n",t,timeTaken,rate );


	}
	return 0;
}
