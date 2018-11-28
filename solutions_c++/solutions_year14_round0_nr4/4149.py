#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

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

static int compare (const void * a, const void * b) {
	if (*(double*)a > *(double*)b) return 1;
	else if (*(double*)a < *(double*)b) return -1;
	else return 0;  
}

int main()
{
	int T,N,scoreNew,scoreKen,j;
	double a[1000],b[1000];
	scanint(T);
	for (int t = 1; t < (T+1); t++)
	{	
		scoreKen = 0;
		scoreNew = 0;
		j = 0;
		scanint(N);
		for(int i =0;i<N;i++) {
			scanf("%lf",&a[i]);
		}
		for(int i =0;i<N;i++) {
			scanf("%lf",&b[i]);
		}
		qsort(a,N,sizeof(double), compare);
		qsort(b,N,sizeof(double), compare);

		 
		for(int i=0;i<N;i++) {
			while((a[j] - b[i]) < -0.0000001) {
				j++;
				if(j>(N-1)) { break;}
			}
			if(j>(N-1)) { break;}
			if( (a[j] - b[i]) > 0.0000001 ) {
				scoreNew++;
				j++;
				continue;
			}
			if(j>(N-1)) { break;}
		}

		j = 0;
		for(int i=0;i<N;i++) {
			while((b[j] - a[i]) < -0.0000001) {
				j++;
				if(j>(N-1)) { break;}
			}
			if(j>(N-1)) { break;}
			if((b[j] - a[i]) > 0.0000001) {
				scoreKen++;
				j++;
			}
			if(j>(N-1)) { break;}
		}

		printf("Case #%d: %d %d\n",t,scoreNew,N - scoreKen);
	}
	return 0;
}
