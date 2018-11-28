#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <ctime>
#include <deque>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define INF 1000000000000000000ll
#define inf 1000000000
#define ll long long
#define ull unsigned ll
#define mp make_pair
#define pb push_back 
#define F first
#define S second

int t;
char s[105];

int main (){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &t);
	for(int test = 1;test <= t;++ test){
		int n;
		scanf("%d\n", &n);
		gets(s);
		int cur_cnt = 0;
		int res = 0;
		for(int i = 0;i <= n;++ i){
			if(cur_cnt < i){
				res += i - cur_cnt;
				cur_cnt += i - cur_cnt;
			}
			cur_cnt += s[i] - '0';
		}
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}       