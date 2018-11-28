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

int T;
double C, F, X, ti, prev;
double rate, temp, ans;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("Bout.txt", "w", stdout);
	cin >> T;
	for(int t=1 ; t<=T ; t++){
		cin >> C >> F >> X;
		rate = 2;
		ti = 0;
		prev = X/rate;
		while(1){
			ti += C/rate;
			rate += F;
			temp = ti + X/rate; 
			if(prev < temp){
				ans=prev;
				break;
			}else{
				prev = temp;
			}
		}
		printf("Case #%d: ",t);
		cout << fixed << setprecision(7) << ans << endl;
	}
	//system("pause");
}