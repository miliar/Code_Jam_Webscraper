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
struct node{
	int x, y, k;
	node(){};
	node(int _x, int _y, int _k):x(_x), y(_y), k(_k){};
};
int main() {
	int cas, c = 1, x, y;
	scanf("%d", &cas);
	while(cas--){
		scanf("%d%d", &x, &y);
		printf("Case #%d: ", c++);
		while(x && x > 0){
			cout << "WE"; x--;
		}
		while(x && x < 0){
			cout << "EW"; x++;
		}
		while(y && y > 0){
			cout << "SN"; y--;
		}
		while(y && y < 0){
			cout << "NS"; y++;
		}
		cout << endl;
	}
    return 0;
}

