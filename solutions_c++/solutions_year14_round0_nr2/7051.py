//Bismillahir Rahmanir Rahim
//#pragma warning(disable:4786)
//#pragma comment(linker,"/STACK:514850816")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <climits>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
using namespace std;

#define mx 100000
#define pii pair < int, int >

#define eps 1e-9
#define pi 2*acos(0.0)

double calcSum(double F, double C, int n) {
	return (C / ((n*F) + 2));
}

double calcMineSum(double X, double F, int n) {
	return (X / ((n*F) + 2));
}

double calcN(double C, double F, double X) {
	return ceil((X / C) - (2 / F) - 1);
}

int main() {
	freopen("G://B-large.in","r",stdin);
	freopen("G://B-large.out","w",stdout);
	int t;
	double C,F,X,n,r, ans, pre, mine, preAns;
	scanf("%d",&t);
	for(int i = 1; i<=t;i++) {
		scanf("%lf %lf %lf",&C,&F,&X);
		pre = 0;
		preAns = 2147483647;
		for(int j = 0;;j++) {
			mine = calcMineSum(X,F,j) + pre;
			if(mine < preAns) {
				preAns = mine;
			} else break;
			pre += calcSum(F,C,j);
		}
		ans = preAns;
		printf("Case #%d: %.7lf\n",i,ans + eps);
	}
	return 0;
}