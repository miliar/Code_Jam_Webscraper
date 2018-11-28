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
#define ii int

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

int n, m;
char s[maxm];

int numberOfFlip(char *s){

	int len = strlen(s), ret = 0;
	char req = '+';

	for (int i = len - 1; i >= 0; i--){
		if (s[i] == req) continue;
		ret++;
		req = (req == '+') ? '-' : '+';
	}

	return ret;
}

int main(){

	freopen("b1.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test, t = 1;
	scanf("%d", &test);
	
	while (test--){
		
		scanf("%s", s); 
		printf("Case #%d: %d\n", t++, numberOfFlip(s));
	}

	return 0;
}


