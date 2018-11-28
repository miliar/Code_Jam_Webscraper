/*
Author      : Rashedul Hasan Rijul ( Silent_coder ).
Created on  : 2014-09-12
*/

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>
using namespace std;

#define maxm 200100
#define inf (1<<29)
#define ii __int64

#define pi  acos(-1.0)
#define eps 1e-9
#define iseq(a,b) (fabs(a-b)<eps)

#define pii pair<int,int>
#define mp  make_pair
#define uu first
#define vv second

ii on(ii n, ii k){ return (n | (1 << k)); }
ii off(ii n, ii k){ return (n - (n&(1 << k))); }
bool chck(ii n, ii k){ return (n&(1 << k)); }

ii mini(ii a, ii b){ if (a<b) return a;  return b; }
ii maxi(ii a, ii b){ if (a>b) return a;  return b; }

int n;
bool seen[10];

bool haveSeenAll(bool seen[]){
	for (int i = 0; i < 10; i++){
		if (!seen[i]) return false;
	}
	return true;
}

void setVal(ii n){
	
	while (n){
		int digit = n % 10; 
		seen[digit] = true;
		n /= 10;
	}
}

int main(){

	freopen("a1.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test, t = 1;
	scanf("%d", &test);
	
	while (test--){
		memset(seen, 0, sizeof(seen));
		scanf("%d", &n);
		
		printf("Case #%d: ", t++);
		if (n == 0){
			puts("INSOMNIA");
			continue;
		}

		ii curr = n;
		ii i;
		for (i = 1;; i++){
			curr = (ii)n*i;
			setVal(curr);
			if (haveSeenAll(seen)){
				printf("%I64d\n", curr);
				break;
			}			
		}		
	}

	return 0;
}


