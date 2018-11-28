#include<iostream>
#include<cmath>
#include<set>
#include<vector>
#include<list>
#include<map>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<stack>
#include<queue>
#include<climits>
#include <string>
#include <sstream>
#include <iomanip>

typedef unsigned long long int ULL;
typedef long long int LL;
typedef unsigned int UINT;

using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)

#ifndef ONLINE_JUDGE
#include <time.h>
#endif

const int L=1000000+2;
int M[L+1];
int A,N;

map<ULL,int> DPS[102];
int DP(int i,ULL l){
	int MIN=L;
	if(i==N)return 0;

	if(DPS[i].find(l)!=DPS[i].end())return DPS[i][l];

	if(l>M[i])MIN=DP(i+1,M[i]+l);
	else{		
		MIN=min(MIN,DP(i+1,l)+1);
		if(2*l-1!=1)MIN=min(MIN,DP(i,2*l-1)+1);
	}
	return DPS[i][l]=MIN;
}


int main(){
	freopen("input.in","r",stdin);
#ifndef _DEBUG 
	freopen ("output.txt","w",stdout);
#endif
	clock_t start = clock();

	
	int T;
	scanf("%d",&T);	
	FOR(tT,0,T){
		scanf("%d%d",&A,&N);
		FOR(i,0,N)scanf("%d",&M[i]);
		sort(M,M+N);
		
		FOR(i,0,N)DPS[i].clear();
		

		printf("Case #%d: ",tT+1);
		printf("%d",DP(0,A));
		printf("\n");
		/*printf("Case #%d: ",tT+1);
		printf("%d",DP(0,E));
		printf("\n");*/
	}

#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}






