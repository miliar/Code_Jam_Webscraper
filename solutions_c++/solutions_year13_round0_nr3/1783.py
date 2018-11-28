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

typedef unsigned long long int ULL;
typedef long long int LL;
typedef unsigned int UINT;

using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)

#ifndef ONLINE_JUDGE
#include <time.h>
#endif

#include<stdio.h>
#include<iostream>
#include<math.h>


ULL TB[]={
	0
,1
,4
,9
, 121
, 484
, 10201
, 12321
, 14641
, 40804
, 44944
, 1002001
, 1234321
, 4008004
, 100020001
, 102030201
, 104060401
, 121242121
, 123454321
, 125686521
, 400080004
, 404090404
, 10000200001
, 10221412201
, 12102420121
, 12345654321
, 40000800004
, 1000002000001
, 1002003002001
, 1004006004001
, 1020304030201
, 1022325232201
, 1024348434201
, 1210024200121
, 1212225222121
, 1214428244121
, 1232346432321
, 1234567654321
, 4000008000004
, 4004009004004
};




int main(){
	freopen("input.in","r",stdin);
#ifndef _DEBUG 
	freopen ("output.txt","w",stdout);
#endif
	clock_t start = clock();
		
	int T;
	scanf("%d",&T);	
	FOR(tT,0,T){
		ULL A,B;
		scanf("%lld%lld",&A,&B);

		ULL* u=upper_bound(TB,TB+sizeof(TB)/sizeof(ULL),B);
		ULL* l=lower_bound(TB,TB+sizeof(TB)/sizeof(ULL),A);

		cout<<"Case #"<<tT+1<<": "<<u-l<<"\n";
	}

#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}






