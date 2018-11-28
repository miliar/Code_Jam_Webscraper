#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
//#include <random>
#include <time.h>

using namespace std;

int main() {
	int i, aktual, zvysok, pocet, a, pozadDlzka, pozadPocet, aktualDlzka;
	double c,f,x,akt,vys;
	scanf("%d", &pocet);
	for (a = 0; a < pocet; a++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		vys = 0.0;
		akt = 2.0;
		while (1) {
			//cout << (x/(akt+f) + c/akt) << endl;
			if (x/akt < (x/(akt+f) + c/akt)) {
				vys = vys + x/akt;
				break;
			}
			else {
				vys = vys + c/akt;
				akt = akt + f;
			}
		}
		printf("Case #%d: %.7lf\n", a+1, vys);
		//cout << "Case #" << a << ": " << vys << endl;
	}
	return 0;
}