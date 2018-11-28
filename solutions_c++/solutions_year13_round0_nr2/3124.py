/*
 * =====================================================================================
 *
 *       Filename:  B.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/2013 11:19:54
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Cong Zhao (), zhaocong89@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define FF(i,n) for(int(i)=0;(i)<(n);(i)++)
#define FOR(i,l,h) for(int(i)=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define CC(n,what) memset(n,what,sizeof(n))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

#define N 105
int lawnmap[N][N];
int rowmax[N];
int colmax[N];
int m,n;
int main(){
	int ncase;
	scanf("%d", &ncase);
	for(int nn = 1; nn <= ncase; nn++){
		scanf("%d%d", &n, &m);
		memset(lawnmap, 0, sizeof(lawnmap));
		memset(rowmax, 0, sizeof(rowmax));
		memset(colmax, 0, sizeof(colmax));

		for(int i = 0; i < n ; i++){
			for(int j = 0; j < m; j++){
				scanf("%d", &lawnmap[i][j]);
				if(lawnmap[i][j] > rowmax[i]){
					rowmax[i] = lawnmap[i][j];
				}
			}
		}

		for(int i = 0; i < m; i++){
			for(int j = 0; j < n; j++){
				if(lawnmap[j][i] > colmax[i]){
					colmax[i] = lawnmap[j][i];
				}
			}
		}
		
		int yes = 1;
		for(int i = 0; i < n; i++){
			if(yes == 0){
				break;
			}
			for(int j = 0; j < m; j++){
				if(lawnmap[i][j] < colmax[j] && lawnmap[i][j] < rowmax[i]){
					yes = 0;
					break;
				}
			}
		}
		if(yes){
			printf("Case #%d: YES\n", nn);
		}
		else{
			printf("Case #%d: NO\n", nn);
		}
	}
	return 0;
}
