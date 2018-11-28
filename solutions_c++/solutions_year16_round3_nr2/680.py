//sort seja trazida
#include <algorithm> 
#include <assert.h>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;
const int MAXN = 1e3;
const int INF  = 1e9;

#define deb(args...) fprintf(stderr,args)
long long dp[MAXN];
int mat[MAXN][MAXN];
int main(){
  int test;
  scanf("%d",&test);
  for(int t=0;t<test;t++){
  	int n;
 	long long m;
  	scanf("%d %lld",&n,&m);
  	/*dp[0]=1;
  	dp[1]=1;
  	for(int i=2;i<n-1;i++){
  		for(int j=0;j<i;j++){
  			dp[i]+=dp[j];
  		}
  	}
  	for(int i=0;i<n;i++){
  		printf("%lld\n",dp[i]);
  	}
  	*/
  	long long mx=(1LL<<(n-2));
  	if(mx<m)printf("Case #%d: IMPOSSIBLE\n",t+1);
  	else if(mx==m){
 		printf("Case #%d: POSSIBLE\n",t+1);
	  	for(int i=0;i<n;i++){
	  		for(int j=0;j<n;j++){
	  			if(i<j)mat[i][j]=1;
	  		}
	  	}
 	  	for(int i=0;i<n;i++){
	  		for(int j=0;j<n;j++){
	  			printf("%d",mat[i][j]);
	  		}
	  		puts("");
	  	}
  	}
  	else{	
		printf("Case #%d: POSSIBLE\n",t+1);
 	  	for(int i=0;i<n;i++){
	  		for(int j=0;j<n;j++){
	  			if(i<j)mat[i][j]=1;
	  		}
	  	}
	  	mat[0][n-1]=0;
	  	for(int i=0;i<n-2;i++){
	  		if((m&(1LL<<i))==0LL){
	  			mat[i+1][n-1]=0;
	  		}
	  	}
 	  	for(int i=0;i<n;i++){
	  		for(int j=0;j<n;j++){
	  			printf("%d",mat[i][j]);
	  		}
	  		puts("");
	  	}
  	}
  }

  return 0;
}
