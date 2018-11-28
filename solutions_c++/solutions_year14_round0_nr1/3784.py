#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <math.h>
#include <cmath>
#include <iomanip>
#include <utility>
#include <limits.h>
#include <stdarg.h>
#include <stdlib.h>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
using namespace std;
#define PI atan(1)*4
#define mp(a,b) make_pair(a,b)
#define ll long long
#define P(str, ...) printf(str, ##__VA_ARGS__)
#define PRINT2D(e, x, y, str) for(int i=0 ; i<x; i++) {for(int j=0 ; j<y ; j++) printf(str, e[i][j]); printf("\n");}

int T, a1, a2, e1[6][6],e2[6][6];

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("Aout.txt", "w", stdout);
	cin >> T;
	for(int t=1 ; t<=T ; t++){
		queue<int> q;
		cin >> a1;
		for(int i=1 ; i<=4 ; i++){
			for(int j=1 ; j<=4 ; j++){
				cin >> e1[i][j];
			}
		}
		cin >> a2;
		for(int i=1 ; i<=4 ; i++){
			for(int j=1 ; j<=4 ; j++){
				cin >> e2[i][j];
			}
		}
		for(int i=1 ; i<=4 ; i++){
			for(int j=1 ; j<=4 ; j++){
				if(e1[a1][i] == e2[a2][j]){
					q.push(e1[a1][i]);
					break;
				}
			}
		}
		printf("Case #%d: ", t);
		if(q.empty()){
			cout << "Volunteer cheated!" << endl;
		}else if(q.size()>1){
			cout << "Bad magician!" << endl;
		}else{
			cout << q.front() << endl;
		}

	}
	//system("pause");
}