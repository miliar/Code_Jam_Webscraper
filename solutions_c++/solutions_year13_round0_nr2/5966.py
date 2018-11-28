#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

//global variables

//some functions
int tb[105][105];

int main() {
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int flag1, flag2;

	int t;
	int n,m;
	scanf("%d", &t);  //case num
	FOR(test, 1, t) {
		scanf("%d%d", &n, &m);
		//int min=100;
		//printf("%d%d\n", n,m);
		REP(i,n) 
			REP(j,m){
		scanf("%d", &tb[i][j]); 
		 //printf("%d\n", tb[i][j]);
		  
		}
		char *result="YES";

		REP(i,n)
		  REP(j,m){
		  if (tb[i][j]==1){
			
			  //check col
			    flag1=1;
		  
			  	REP(a,n){
		       if (tb[a][j]!=1){
		     
		      //if(i==1 && j==0) 
	          //printf("%d%d\n", a, j);  
				   flag1=0;
			       break;
			   }
		       }
              flag2=1;
			  //check row
		      	REP(b,m){
		       if (tb[i][b]!=1){
              // if(i==1 && j==0) 
	          //printf("%d%d\n", i, b);
				   flag2=0; 
			       break;
			   }
			}
			  if (flag1==0 && flag2==0)
			  result="NO";
	
		  }
	
		    
		}
		printf("Case #%d: ", test); //test cases

				printf("%s ", result); //results

			printf("\n");
		
	}

	exit(0);
}
