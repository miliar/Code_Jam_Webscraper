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

typedef unsigned long long int ULONG;
typedef long long int LONG;
typedef unsigned int UINT;

using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)

#ifndef ONLINE_JUDGE
#include <time.h>
#endif

#include<stdio.h>
#include<iostream>
#include<math.h>

const int L=100+2;





int main(){
	freopen("input.in","r",stdin);
#ifndef _DEBUG 
	freopen ("output.txt","w",stdout);
#endif
	clock_t start = clock();

	int A[L][L],MAX[2][L];
	
	int T;
	scanf("%d",&T);	
	FOR(tT,0,T){
		int N,M;
		scanf("%d%d",&N,&M);
		FOR(i,0,N){
			FOR(j,0,M){
				scanf("%d",&A[i][j]);				
			}
		}
		
		FOR(i,0,M){
			MAX[0][i]=-1;
		}
		FOR(i,0,N){
			MAX[1][i]=-1;
		}
		
			

		FOR(i,0,N){
			FOR(j,0,M){
				MAX[0][j]=max(A[i][j],MAX[0][j]);
				MAX[1][i]=max(A[i][j],MAX[1][i]);
			}
		}

		printf("Case #%d: ",tT+1);

		FOR(i,0,N){
			FOR(j,0,M){
				if(!(A[i][j]>=MAX[0][j] || A[i][j]>=MAX[1][i])){
					printf("NO");
					goto E;
				}
			}
		}


		printf("YES");		
		E:
		printf("\n");
	}

#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}






