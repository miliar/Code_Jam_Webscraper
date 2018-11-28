#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<queue>
#include<vector>
#include <string>

#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define println(X) printf("%d\n",(X))
#define PB push_back
#define MP make_pair
using namespace std;

int main(){
	freopen("omino.in", "r", stdin);
	freopen("omino.out", "w", stdout);
	DRI(T);
	for (int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		DRIII(X, R, C);
		if (X == 1){
			cout << "GABRIEL\n";
		}
		else if (X == 2){
			if ((R * C) % 2 == 0){
				cout << "GABRIEL\n";
			}
			else{
				cout << "RICHARD\n";
			}
		}
		else if (X == 3){
			if ((R * C) % 3 != 0){
				cout << "RICHARD\n";
			}
			else if (R == 1 || C == 1){
				cout << "RICHARD\n";
			}
			else{
				cout << "GABRIEL\n";
			}
		}
		else if (X == 4){
			if ((R * C) % 4 != 0){
				cout << "RICHARD\n";
			}
			else if (R == 1 || C == 1 || R == 2 || C == 2){
				cout << "RICHARD\n";
			}
			else{
				cout << "GABRIEL\n";
			}
		}
	}
	return 0;
}