#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <limits>

#define maxN(a,b) ((a>b)?(a):(b))
#define minN(a,b) ((a<b)?(a):(b))
#define INF (int)10e9
#define ABS(n)	((n>0)? n:(-1*n))
#define NINF -(int)10e9
#define eps 10e-9
#define WORDSIZE 31

using namespace std;

typedef vector<int> V;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;
typedef vector<pair<int, int> > VPII;


	  //U  D  L  R
int dx[] = {0, 0, 1, -1};
int dy[] = {1,-1, 0, 0};
// numeric_limits<int>::min();
bool sortPair(const PII p1, const PII p2) {
	if(p1.first > p2.first){
		return false;	
	} else if( p1.second > p2.second ) {
		return false;	
	} 
	return true;
}

int main() {
	int tc;
	int a, row;
	scanf("%d", &tc);
for(int t = 1; t <= tc; t++){
	int count[17] = {}, cnt = 0, num;
	scanf("%d", &row);	
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			scanf("%d", &a);	
			if( row == i+1) count[a] += 1 ;
		}	
	}
	scanf("%d", &row);	
	for(int i = 0; i < 4; i++){
		
		for(int j = 0; j < 4; j++){
			scanf("%d", &a);	
			if( row == i+1) if(count[a] == 1) {cnt++; num = a;}
		}	
	}
	if( cnt == 1) printf("Case #%d: %d\n", t, num);
	else if( cnt > 1) printf("Case #%d: Bad magician!\n", t);
	else printf("Case #%d: Volunteer cheated!\n", t);
}
	return 0;
}

