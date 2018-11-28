/*************************************************************************
Author: zjut_polym
Created Time:   2014/4/13 9:09:57
File Name: D.cpp
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
#define N 1005
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------
double Naomi[N], Ken[N];
int n;
int solve1(int Nl, int Nr, int Kl, int Kr){
	int Na = Nl, Ke = Kl, ans = 0;
	while(Na < Nr){
		while(Ke < Kr && Naomi[Na] > Ken[Ke]) Ke++;
		if(Ke == Kr) ans++;
		else Ke++;
		Na++;
	}
	return ans;
}
int check(int Nl, int Nr, int Kl, int Kr){
	int Na = Nl, Ke = Kl, ans = 0;
	while(Ke < Kr){
		while(Na < Nr && Naomi[Na] < Ken[Ke]) Na++;
		if(Na < Nr) {ans++; Na++;}
		Ke++;
	}
	return ans;
}
int solve2(){
	int ans, i;
	ans = 0;
	for(i = 0; i < n; i++){
		ans = max(ans, check(i, n, 0, n-i));
	}
	return ans;
}
int main() {
	int T, cas = 1;
	cin >> T;
	while(T--){
		cin >> n;
		printf("Case #%d: ", cas++);
		for(int i = 0; i < n; i++){
			cin >> Naomi[i];
		}
		for(int i = 0; i < n; i++){
			cin >> Ken[i];
		}
		sort(Naomi, Naomi+n);
		sort(Ken, Ken+n);
//		cout << endl;
//		for(int i = 0; i < n; i++){
//			cout << Naomi[i] << " ";
//		}
//		cout << endl;
//		for(int i = 0; i < n; i++){
//			cout << Ken[i] << " ";
//		}
//		cout << endl;
		cout << solve2() << " " << solve1(0,n,0,n) << endl;
	}
    return 0;
}

