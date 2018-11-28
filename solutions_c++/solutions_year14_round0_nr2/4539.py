/*************************************************************************
Author: zjut_polym
Created Time:   2014/4/12 21:35:53
File Name: B.cpp
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


int main() {
	int T, cas = 1;
	cin >> T;
	while(T--){
		printf("Case #%d: ", cas++);
		double sp = 2.0, C, F, X, ans = 0;
		cin >> C >> F >> X;
		while(1){
			if(C / sp + X / (sp + F) < X / sp){
				ans += C / sp;sp = sp + F; 
			}
			else{
				ans += X / sp; break;
			}
		}
		printf("%.7lf\n", ans);
	}
    return 0;
}

