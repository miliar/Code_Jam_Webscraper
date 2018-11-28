// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

double eps = 1e-9;
int T;
int n;
double v, x;
pair<double, double> zdroje[111];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("vstup.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for (int t = 1; t <= T; t++){

		cin >> n >> v >> x;
		//scanf("%f %f", &v, &x);
		double tmp1, tmp2;
		for (int j = 0; j < n; j++){

			cin >> zdroje[j].first >> zdroje[j].second;
		}
		//sort(zdroje, zdroje + n);
		bool poss = true;
		double rslt;
		/*
		if (n == 1){
			if (x == zdroje[0].second){
				rslt = v / zdroje[0].first;
			}
			else{ poss = false; }
		}

		if (n == 2){
			double ans = 1e9+1;
			if (x == zdroje[0].second){
				ans = min(ans,  v / zdroje[0].first);
			}
			if (x == zdroje[1].second){
				ans = min(ans, v / zdroje[1].first);
			}
			if (x == zdroje[0].second && v == zdroje[1].second){
				ans = min(ans, v / (zdroje[0].first+ zdroje[1].first));
			}
			if ((zdroje[0].second < x && zdroje[1].second > x) || (zdroje[1].second < x && zdroje[0].second > x)){
				double alfa = (v*x - v*zdroje[1].second) / (zdroje[0].second - zdroje[1].second);
				ans = min(ans, max(alfa / zdroje[0].first, (v - alfa) / zdroje[1].first));
			}
			rslt = ans;
			if (rslt > 1e9){ poss = false; }
		}
		*/
		double zmax = zdroje[0].first;
		double zmin = zmax;
		for (int i = 1; i < n; i++){
			zmin = min(zmin, zdroje[i].first);
			zmax = max(zmax, zdroje[i].first);
		}

		double dol = v / (n*zmax);
		double hor = 2*v / zmin;
		double limit = hor/2+eps;

		while (hor - dol > eps){
			double pul = (dol + hor) / 2;
			double vtepl = 0;
			double vchlad = 0;
			double vako = 0;
			double etepl = 0;
			double echlad = 0;
			
			for (int i = 0; i < n; i++){
				if (zdroje[i].second == x){ vako += zdroje[i].first*pul; }
				else if (zdroje[i].second > x) {
					vtepl += zdroje[i].first * pul;
					etepl += zdroje[i].first * pul * zdroje[i].second;
				}
				else{
					vchlad += zdroje[i].first * pul;
					echlad += zdroje[i].first * pul * zdroje[i].second;
				}
			}
			double vsk = v - vako;
			if (vsk <= 0){ hor = pul; continue; }
			double alfa = (vsk*x*vchlad - vsk*echlad) / (vchlad*etepl - vtepl*echlad);
			double beta = (vsk - alfa*vtepl) / vchlad;
			if (0 <= alfa && alfa <= 1 && 0<=beta && beta <= 1){ hor = pul; }
			else{ dol = pul; }
			if (dol > limit || hor < 0) { poss = false; break; }
		}

		if (poss){
			printf("Case #%d: %4.10f\n", t, dol);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}

	return 0;
}

