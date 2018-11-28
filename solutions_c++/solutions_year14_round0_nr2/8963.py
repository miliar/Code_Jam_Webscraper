/*
 * B-Cookie_Clicker_Alpha.cpp
 *
 *  Created on: Apr 13, 2014
 *      Author: Yasser
 */

#include<iostream>
using namespace std;

int main() {

	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	double C, F, X, time = 0, c, tot;
	scanf("%d",&T);
	for(int tt=0;tt<T;tt++) {
		cin >> C >> F >> X;
		time = 0, c=2 , tot = 0;

		while(true){

			double t1 = X/c;
			double t2 = C/c + X/(c+F);
			if(t1 - t2 > 1e-9){
				tot += C/c;
				c += F;
			} else {
				tot += t1;
				break;
			}
		}

		printf("Case #%d: %.7f\n",tt+1, tot);

	}

	return 0;
}
