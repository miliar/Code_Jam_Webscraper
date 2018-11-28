//#define _CRT_SECURE_NO_WARNING
#include <queue>
#include <iostream>
#include <fstream>
#include <map>
#include <vector> 
#include <set>
#include <string>
#include <math.h>
#include <cmath>
#include <stdio.h> 
#include <stdlib.h>
using namespace std;

typedef long long ll; 



int main(){



	ofstream fout;
	fout.open("out.txt");
	int t;
	cin >> t;

	for (int q = 0; q < t; q++){
		int sMax;
		cin >> sMax;
		string st;
		cin >> st;

		int rest = 0;
		int claps = 0;

		for (int i = 0; i < st.size(); i++){
			int num = st[i] - '0';
			if (num > 0){
				if (claps < i){
					rest += i - claps;
					claps += (i - claps) + num;
				}
				else {
					claps += num;
				}
			}
		}

		fout << "Case #" << q + 1 << ": " << rest << endl;
	}
	 
	return 0;
}