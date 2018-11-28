#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <time.h>
using namespace std;
#pragma comment(linker, "/STACK:100000000")

#define mp make_pair
#define pb push_back 
#define ll long long
#define sz(x) (int)(x).size()



int main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	//freopen("onlyone.in","rt",stdin);
	//freopen("onlyone.out","wt",stdout);
	
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++) {
		int res = 0;
		int n;
		scanf("%d", &n);
		n++;
		string s;
		cin >> s;
		int cnt = 0;
		for(int i = 0; i < n; i++) {
			int diff = i - cnt;
			if(diff > 0) {
				cnt += diff;
				res += diff;
			}
			cnt += (int)(s[i] - '0');
		}


		printf("Case #%d: %d\n", test, res);
	}

    return 0;
}