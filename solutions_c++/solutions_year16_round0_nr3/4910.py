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

#define count blergh

typedef long long ll;
using namespace std;

int fat(ll num){
	for(ll i=2;i*i<=num;i++)
		if(num%i == 0)
			return i;
	return 1;
}

main(){

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){

		int n,k;
		scanf("%d%d",&n,&k);
		int cont = 0;
		printf("Case #1:\n");
		for(int i=0;i<(1<<16);i++){

			if(i%2 == 0) continue;
			if((i&(1<<15)) == 0) continue;

			int ok = 1;
			
			int aux = i;
			while(aux){
				if(aux%4 == 1 || aux%4 == 2)
					ok = 0;
				aux /= 4;
			}

			if(!ok) continue;
			cont++;
			if(cont > 50)
				break;

			for(int j=15;j>=0;j--)
				printf("%d",(i&(1<<j))?1:0);
			for(int i=2;i<=10;i++)
				printf(" %d",i+1);
			printf("\n");

		}

	}

}
