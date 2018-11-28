#pragma comment(linker, "/STACK:1000000000")
#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#define rep(x, a, b) for(int (x) = (a); (x) < int(b); ++(x))
#define Wait cin.sync(); cin.get();
#define INF_INT 2000000000;
#define INF 0x3F3F3F3F
#define y1 qwerty 
#define EPS 1e-6
using namespace std;
typedef long long                  ll;
typedef pair<long long, long long> pll;
typedef pair<int, int>             pii;
typedef pair<double, int>          pdi;
typedef pair<string, string>       pss;

int T, l, x;
int pref[111111], suf[111111], arr[111111];
string s, small;
int X;
// 1 - 1, 2 - i, 3 - j, 4 - k
int get(int f, int s){
	if (f == 0) return s;
	if (s == 0) return f;
	int zn = 1;
	if (f < 0) zn *= -1, f = abs(f);
	if (s < 0 ) zn *= -1, s = abs(s);
	if (f == 1) return s*zn;
	if (f == 2){
		if (s == 1) return f*zn;
		if (s == 2) return -1 * zn;
		if (s == 3) return 4 * zn;
		if (s == 4) return -3 * zn;
	}
	if (f == 3){
		if (s == 1) return f*zn;
		if (s == 2) return -4 * zn;
		if (s == 3) return -1* zn;
		if (s == 4) return 2 * zn;
	}
	if (f == 4){
		if (s == 1) return f*zn;
		if (s == 2) return 3 * zn;
		if (s == 3) return -2 * zn;
		if (s == 4) return -1 * zn;
	}
}
int getmid(int l, int r){
	if (get(get(l, 1), r) == X) return 1;
	if (get(get(l, -1), r) == X) return  -1;
	if (get(get(l, 2), r) == X) return 2;
	if (get(get(l, -2), r) == X) return -2;
	if (get(get(l, 3), r) == X) return 3;
	if (get(get(l, -3), r) == X) return -3;
	if (get(get(l, 4), r) == X) return 4;
	if (get(get(l, -4), r) == X) return -4;
 }

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> T;	
	for (int t = 0; t < T; ++t){
		cout << "Case #" << t + 1 << ": ";
		cin >> l >> x;
		cin >> small;
		s.clear();
		memset(suf, 0, sizeof suf);
		memset(pref, 0, sizeof pref);
		memset(arr, 0, sizeof arr);
		for (int i = 0; i < x; ++i) s += small;
		int all = x * l;
		//cout << s << endl;
		if (all < 3){
			cout << "NO" << endl;
			continue;
		}
		//cout << all << "  " << s.size() << endl;
		
		for (int i = 0; i < s.size(); ++i){
			arr[i+1] = s[i] - 'i' + 2;
		}
		for (int i = 1; i <= all; ++i){
			pref[i] = get(pref[i - 1], arr[i]);
			//cout << pref[i] << " ";
		}
		X = pref[all];
		//cout << "end" << endl;
		for (int i = all; i > 0; --i){
			suf[i] = get(arr[i], suf[i + 1]);
			//cout << suf[i] << " ";
		}
		int I = 1, J = all;
		int ok = 0;
		//cout << "X = " << X << endl;
		while (I < J){
			//cout << pref[I] << " " << suf[J] << endl;
			if (pref[I] != 2) I++;
			else if (suf[J] != 4) J--;
			else{
				//cout << "mid = " << getmid(pref[I], suf[J]) << endl;
				if (getmid(pref[I], suf[J]) == 3) {
					cout << "YES" << endl;
					ok = 1;
					break;
				}
				else{
					cout << "NO" << endl;
					ok = 1;
					break;
				}
			}
		}
		if(!ok)cout << "NO" << endl;

	}
	
	//printf("TIME: %.3lf\n", (long double)(clock()) / CLOCKS_PER_SEC);
	Wait
	return 0;
}