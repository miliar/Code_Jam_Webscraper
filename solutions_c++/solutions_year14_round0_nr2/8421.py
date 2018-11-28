#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
const int maxn = 1000000 + 10;
typedef long long LL;
int one[100][100],two[100][100];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int testc,ca=0;
	int count=0;

	double pi=2;
	double pre,next,time=0,x,c,f;
    scanf("%d", &testc);
	
    while (testc--) {
		        printf("Case #%d: ", ++ca);
				 scanf("%lf%lf%lf", &c,&f,&x);
				 time=0;
				 pi=2;
				 pre=x/pi;
				 next=(c/pi)+(x/(pi+f));
				 while(pre>next)
				 {
					 time=time+(c/pi);
					 pre=next;
					 pi=pi+f;
					 next=time+(c/pi)+(x/(pi+f));
				 }
				 printf("%lf \n",pre);
    }
    return 0;
}

