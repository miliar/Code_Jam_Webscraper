#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
const int N = 1e6 + 5;
int t, n;
string g;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> n >> g;
		int sum = 0;
		int res = 0;
		for (int i = 0; i < g.size(); ++i){
			g[i] -= '0';
			if (g[i]){
				if (i > sum){
					res += i - sum;
					sum = i;
				}
				sum += g[i];
			}
		}
		printf("Case #%d: %d\n", k, res);
	}
}