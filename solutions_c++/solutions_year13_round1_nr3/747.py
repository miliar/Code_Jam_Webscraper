#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int t,k;
typedef long long ll;
const double eps = 1e-1;


int val[15];

map<int, map<int, double> > mapa;
map<int, map<int, double> > mapa2;

void calc(double chance, int tot, int prod){
	if(tot > 99){
		chance *= 0.25/2;
		mapa[tot][prod] += chance;
		mapa[tot][prod*(tot%10)] += chance;
		
		mapa2[prod][tot] += chance;
		mapa2[prod*(tot%10)][tot] += chance;
		return;
	}
	for(int i = tot%10; i < 6; ++i){
		calc(chance/2, tot*10+i, prod);
		calc(chance/2, tot*10+i, prod*(tot%10));
	}
}

double resp[1000];
int pode[1000];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	for(int i = 2; i < 6; ++i){
		calc(1.0, i, 1);
	}
	scanf("%d", &t);
	int r, n, m;
	for(int _ = 1; _ <= t; ++_){
		printf("Case #%d:\n", _);
		scanf("%d %d %d %d", &r, &n, &m, &k);
		for(int i = 0; i < r; ++i){
			memset(pode, 0, sizeof pode);
			memset(resp, 0, sizeof resp);
			for(int j = 0; j < k; ++j){
				scanf("%d", val+j);
				int x = val[j];
				for(map<int,double>::iterator it = mapa2[x].begin(); it != mapa2[x].end(); ++it){
					resp[it->first] += it->second;
					pode[it->first]++;
				}
			}
			int ind = 0;
			double maior = 0;
			for(int j = 222; j < 556; ++j){
				if(pode[j] == k){
					//printf("%d pode com chance %lf\n", j, resp[j]);
					if(resp[j] > maior){
						maior = resp[j];
						ind = j;
					}
				}
			}
			printf("%d\n", ind);
		}
	}
	return 0;
}
