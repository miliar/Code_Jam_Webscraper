// =====================================================================================
//       Filename:  B.cpp
//    Description:  
//        Created:  04/13/2013 01:42:01 PM
//         Author:  BrOkEN@!
// =====================================================================================

#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define FOR(i,a,b) for(typeof((a)) i=(a); i < (b) ; ++i)       
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin(); it != (x).end() ; ++it)   
#define MAX 100


using namespace std;

typedef pair<int,int> PI;
typedef vector<PI> VI;

int N=0,M=0;
int f[MAX][MAX];
int a[MAX][MAX];

void cutByROW(int h){
	FOR(r,0,N){
		bool cut=true;
		FOR(c,0,M){
			if(f[r][c]==a[r][c] && h<f[r][c]){
				cut=false;
				break;
			}
		}

		if(cut){	//make a cut
			FOR(c,0,M){	a[r][c]=h;	}
		}
		
	}
}

void cutByCOL(int h){
	FOR(c,0,M){
		bool cut=true;
		FOR(r,0,N){
			if(f[r][c]==a[r][c] && h<f[r][c]){
				cut=false;
				break;
			}
		}

		if(cut){	//make a cut
			FOR(r,0,N){	a[r][c]=h;	}
		}
	}
}

int solve(){
	for(int h=99;h>0;h--){
		cutByROW(h);
		cutByCOL(h);		
	}

//	FOR(i,0,N){	FOR(j,0,M){	printf("%d ",a[i][j]);	} printf("\n");	}
	FOR(i,0,N){	
		FOR(j,0,M){
			if(f[i][j]!=a[i][j]){
				return false;
			}	
		} 
	}
	return true;
}


int main(){
	int T=0;
	scanf("%d",&T);
	char op[2][4]={"NO","YES"};
	FOR(t,1,T+1){
		scanf("%d %d\n",&N,&M);

		FOR(i,0,MAX){	FOR(j,0,MAX){	f[i][j]=0;a[i][j]=100;	}	}
		

		FOR(i,0,N){
			FOR(j,0,M){
				scanf("%d",&f[i][j]);
			}
		}
	
		printf("Case #%d: %s\n",t,op[solve()]);
	}
	return 0;
}

