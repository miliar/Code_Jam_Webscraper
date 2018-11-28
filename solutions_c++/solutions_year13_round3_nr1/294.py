/*************************************************************************
Author: zjut_polym
Created Time:   2013/4/27 8:44:13
File Name: codejam.cpp
************************************************************************/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>
#include <queue>
using namespace std;


//----------------------[ZJUT-polym for div2]-------------------------------------
#define ll long long
#define MOD 1000000007
#define PII pair<int, int>
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define _mst(buf, val) memset(buf, val, sizeof(buf))
#define rep(i, l, r) for(i = (l); i <= (r); i++)
#define srep(i, l, r) for(i = (l); i >= (r); i--)
#define repi(it, c) for(typeof(c.begin())it = c.begin(); it != c.end(); it++)
#define inf 0x3f3f3f3f
#define N 100005
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------
char ch[5] = {'a', 'e', 'i', 'o', 'u'};
char cmd[1000006];
int pos[1000006];
int main() {
	int cas, size, m, c = 1;
	scanf("%d", &cas);
	while(cas--){
		size = 0;
		scanf("%s%d", cmd + 1, &m);
		int len = strlen(cmd + 1), i = 1, l = 1;
		ll ans = 0;
		while(i <= len){
			while(i <= len && size < m){
				bool flag = false;
				for(int j = 0; j < 5 && !flag; j++){
					if(ch[j] == cmd[i]){
						flag = true;
					}
				}
				if(!flag){
					i++; size++;
				}
				else{
					i++; size = 0;
				}
			}
			if(size == m){
				ans += (ll)(i - m - l + 1) * (len - i + 2);
				l = i - m + 1;
				size--;
			}
		}
		printf("Case #%d: %I64d\n", c++,  ans);
	}
    return 0;
}

