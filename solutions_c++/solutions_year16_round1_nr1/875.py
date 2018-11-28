﻿/*
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

#define maxm 2010
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

int main(){

	int i, j, k, l, test, t = 1;

	freopen("a2.in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d", &test);

	while (test--){

		scanf("%s", s);

		string ans = "";

		for (i = 0; s[i]; i++){
			if (ans.size() == 0){
				ans = s[i];
				continue;
			}
			if (ans.at(0) <= s[i]){
				ans = s[i] + ans;
			}
			else{
				ans = ans + s[i];
			}
		}
		
		printf("Case #%d: ", t++);
		cout << ans << endl;
	}

	return 0;
}

