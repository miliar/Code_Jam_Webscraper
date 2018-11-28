#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("B.in","r");
FILE *out=fopen("B.out","w");

int n;

vector < string > ar,nar;

int main()
{
	int i,j,k,test,tests;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		fscanf(in,"%d\n",&n);
		ar.resize(0);
		char junk[1000];
		int ret = 0;
		for(i=0;i<n;i++) {
			fscanf(in,"%s",junk);
			ar.push_back(junk);
		}
		int tt[10];
		for(i=0;i<n;i++){
			tt[i] = i;
		}
		do {
			int vis[512];
			CLR(vis,0);
			int flag = 0;
			char cur = 'Z';
			for(i=0;i<n;i++) {
				for(j=0;j<ar[tt[i]].size();j++) {
					if(ar[tt[i]][j] != cur) {
						vis[cur] = 1;
						cur = ar[tt[i]][j];
					}
					if (vis[cur]){
						flag = 1;
						break;
					}
				}
				if (flag)break;
			}
			if (!flag)ret++;
		}while(next_permutation(tt,tt+n));

		fprintf(out,"Case #%d: %d\n", test,ret);
	}
	return 0;
}
