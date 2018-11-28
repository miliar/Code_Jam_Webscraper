#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdlib>
#include <set>
#include <string>
#include <vector>
#include <cmath>
#define MAX 100005

typedef long long Int;
using namespace std;
//vector<int> g[MAX];
//int usd[MAX];


int a[1005],b[1005];

bool cmp( int x, int y ){
	return a[x] < a[y];
}

int go(){
	int n ;
	scanf("%d",&n);
	for( int i = 0; i < n; i++) {
		scanf("%d",a+i);
		b[i] = i;
	}
	int res = 0;
	int x = 0, y = n - 1;
	for( int i = 0; i < n; i++){
		sort( b , b + n, cmp );
		if ( b[i] - x < y - b[i] ){
			for( int j = b[i] ; j > x; j--){
				swap( a[j], a[j-1] );
				res++;
			}
			x++;
		}else{
			for( int j = b[i] ; j < y ;j++){
				swap( a[j], a[j+1] );
				res++;
			}	
			y--;
		}
	}	
	return res;
}

int main(){

	int run;
	scanf("%d",&run);
	for( int r = 1; r <= run; r++){
		printf("Case #%d: %d\n",r,go());
	}

	return 0;
}
