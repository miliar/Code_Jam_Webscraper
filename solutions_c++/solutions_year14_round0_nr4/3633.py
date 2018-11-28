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

int T, N;
double e[1005], f[1005];

int main(){
	freopen("D-large.in", "r", stdin);
	freopen("Dout2.txt", "w", stdout);
	cin >> T;
	for(int t=1 ; t<=T ; t++){
		cin >> N;
		for(int i=0 ; i<N ; i++){
			cin >> e[i];
		}
		for(int j=0 ; j<N ; j++){
			cin >> f[j];
		}
		sort(e, e+N);
		sort(f, f+N);
		int p=0, q=0;

		while(p<N && q<N){
			if(e[p]<f[q]){
				p++;
			}else{
				q++;
				p++;
			}
		}

		int s=0, r=N-1, u=N-1;
		while(s<r || u>=0){
			if(e[u]>f[r]){
				s++;
			}else{
				r--;
			}
			u--;
		}
		printf("Case #%d: ",t);
		cout << q << ' ' << s << endl;
	}
	//system("pause");
}