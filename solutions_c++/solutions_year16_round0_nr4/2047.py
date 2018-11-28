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

ii k, c, s;
vector<ii>ans;

ii poww(ii b, ii p){
	if (!p) return 1;
	return poww(b, p - 1)*b;
}

void findSolution(ii k, ii c){

	ans.clear();
	
	ii currNode = 1,lim = poww(k,c);
	int upto = 0;
	while (true){
		upto++;
		currNode = upto;
		for (int c1 = 2; c1 <= c; c1++){
			upto++;
			if (upto >= k) upto = k;
			currNode = (currNode - 1)*k + upto;
			if (currNode >= lim){
				currNode = lim;
				break;
			}
		}
		ans.push_back(currNode);
		if (upto >= k) break;
	}

}

int main(){

	freopen("d1.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test, t = 1;
	scanf("%d", &test);
	
	while (test--){
		
		scanf("%I64d %I64d %I64d", &k, &c, &s);

		findSolution(k, c);

		printf("Case #%d:", t++);
		if (ans.size() > s){
			puts(" IMPOSSIBLE");
			continue;
		}
		for (int i = 0; i < ans.size(); i++){
			printf(" %I64d", ans[i]);
		}
		puts("");
	}

	return 0;
}


