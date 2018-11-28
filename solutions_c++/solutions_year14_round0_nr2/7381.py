#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<list>
#include<string>
#include<set>
#include<map>
#include<iomanip>
#include<sstream>
#include<string.h>
#include<math.h>
#include<functional>
#include<deque>
#include<fstream>
#define eps 1e-9
using namespace std;

double c, f, x;
int main(){
	//freopen("test.txt", "r", stdin);
	//freopen("problem2LargeSol.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i){
		scanf("%lf %lf %lf", &c, &f, &x);
		double res = 10000000, toadd = 0.0, rate = 2.0;
		while (1){
			double curres = toadd + x / rate;
			if (res > curres){
				res = curres;
			}
			else break;
			toadd += c / rate;
			rate += f;
		}
		printf("Case #%d: %.7lf\n", i, res);
	}

	return 0;
}
