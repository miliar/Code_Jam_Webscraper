#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <string>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define inf 1000000007
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 50500

typedef long long ll;
using namespace std;

int f[3030];

main(){

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){

		int n;
		scanf("%d",&n);

		for(int i=0;i<3000;i++)
			f[i] = 0;

		for(int i=0;i<n*(2*n-1);i++){
			int u;
			scanf("%d",&u);
			f[u]++;
		}

		printf("Case #%d: ",t);
		int k =0 ;
		for(int i=0;i<3000;i++)
			if(f[i]%2){
				printf("%d",i);
				k++;
				if(k != n)
					printf(" ");
			}
		printf("\n");

	}

}
