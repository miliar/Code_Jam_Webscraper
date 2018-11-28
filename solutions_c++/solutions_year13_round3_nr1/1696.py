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
#include<fstream>

typedef unsigned long long int ULL;
typedef long long int LL;
typedef unsigned int UINT;

using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)

#ifndef ONLINE_JUDGE
#include <time.h>
#endif

#define V(x) ( (x)=='a' || (x)=='e' || (x)=='i' || (x)=='o' || (x)=='u' )

char S[1000000+2],L;
int N;
LL DP(int i){
	if(i==L)return 0;
	LL s=0,t=0;
	for(int a=i;a<L;a++){
		if(V(S[a]))t=0;
		else t++;
		if(t>=N){
			s+=L-a;
			break;
		}
	}
	return DP(i+1)+s;
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
		
		
		scanf("%s%d",S,&N);
		L=strlen(S);
		

		printf("Case #%d: ",tT+1);
		printf("%lld",DP(0));
		printf("\n");
	}

#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}






