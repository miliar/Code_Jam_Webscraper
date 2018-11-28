/*
 * proD.cpp
 *
 *  Created on: 2013-4-13
 *      Author: york
 */

#include<iostream>
#include <cmath>
using namespace std;

int main(){
	int m;
	int a,b;
	int sqrta,sqrtb;
	int tmp;
	int count = 0;
	cin >> m;
	for(int i=1;i<=m;++i){
		cin >> a >> b;
		sqrta = sqrt(a);
		if(sqrta*sqrta != a){
			++sqrta;
		}
		sqrtb = sqrt(b);
		count = 0;
		for(int j=sqrta;j<=sqrtb;++j){
				if(j > 10 && (j%10 != j/10)){
					continue;
				}
				tmp = j * j;
				if(tmp < 10){
					++count;
				}
				else if(tmp > 10 && tmp < 100){
					if(tmp%10 == tmp/10){
						++ count;
					}
				}
				else if(tmp > 100 && tmp < 1000){
					if(tmp%10 == tmp/100){
							++ count;
					}
				}
		}
		cout << "Case #" << i << ": " << count << endl;
	}
}

