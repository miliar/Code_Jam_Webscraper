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

int T;
int X, C, R;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> T;
	for (int t = 0; t < T; ++t){
		cout << "Case #" << t + 1 << ": ";
		cin >> X >> C >> R;
		if (X == 1){
			cout << "GABRIEL" << endl;
			continue;
		}
		if (C < X && R < X){
			cout << "RICHARD" << endl;
			continue;
		}
		if ((C * R - X) % X){
			cout << "RICHARD" << endl;
			continue;
		}
		///////////////////////////////////////////
		if (R == 1){
			if (X == 2 && !(C % 2)) cout << "GABRIEL" << endl;
			else cout << "RICHARD" << endl;
			continue;
		}
		if (C == 1){
			if (X == 2 && !(R % 2)) cout << "GABRIEL" << endl;
			else cout << "RICHARD" << endl;
			continue;
		}
		///////////////////////////////////////////
		if (R == 2 || C == 2){
			if (X == 2) cout << "GABRIEL" << endl;
			else if (X == 3) cout << "GABRIEL" << endl;
			else if (X == 4) cout << "RICHARD" << endl;
			continue;
		}
		///////////////////////////////////////////
		if (R == 3 || C == 3){
			if (X == 2) cout << "GABRIEL" << endl;
			else if (X == 3) cout << "GABRIEL" << endl;
			else if (X == 4) cout << "GABRIEL" << endl;
			continue;
		}
		///////////////////////////////////////////
		if (R == 4 || C == 4){
			if (X == 2) cout << "GABRIEL" << endl;
			else if (X == 3) cout << "RICHARD" << endl; 
			else if (X == 4) cout << "GABRIEL" << endl;
			continue;
		}
		

	}

	//printf("TIME: %.3lf\n", (long double)(clock()) / CLOCKS_PER_SEC);
	Wait
	return 0;
}