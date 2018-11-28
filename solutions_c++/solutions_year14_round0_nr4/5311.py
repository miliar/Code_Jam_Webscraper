#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<sstream>
using namespace std;
typedef long long ll;
double v;
int t, n;
vector<double>a, d;
set<double>b;
int main(){
	freopen("D-small-attempt3.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 1; k <= t; ++k){
		scanf("%d", &n);
		a.clear();
		b.clear();
		d.clear();
		for (int i = 0; i < n; ++i){
			scanf("%lf", &v);
			a.push_back(v);
		}
		for (int i = 0; i < n; ++i){
			scanf("%lf", &v);
			b.insert(v);
			d.push_back(v);
		}
		sort(a.begin(), a.end());
		sort(d.begin(), d.end());
		int second = 0;
		for (int i = 0; !second && i < n; ++i){
			set<double>::iterator it = b.lower_bound(a[i]);
			if (it == b.end())
				second = n - i;
			else b.erase(*it);
		}
		int naomi = 0;
		int ken = n - 1;
		while (ken >= 0 && d[ken]>a[n - 1]){
			--ken;
			++naomi;
		}
		int p = 0;
		while (p <= ken && naomi < n && a[naomi] < d[p])
			++naomi;
		printf("Case #%d: %d %d\n", k, n - naomi, second);
	}
}