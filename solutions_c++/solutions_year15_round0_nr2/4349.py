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


vector<int> v;

int fn(int k){
	int rest = k;

	for (int i = 0; i < v.size(); i++){
		rest += (v[i] - 1) / k;
	}
	return rest;
}

int main(){



	ofstream fout;
	fout.open("out.txt");
	int t;
	cin >> t;

	for (int q = 0; q < t; q++){

		int d;
		cin >> d;

		v.resize(d);

		int mx = 0;

		for (int i = 0; i < v.size(); i++){
			cin >> v[i];
			mx = max(mx, v[i]);
		}


		int rest = 10000000;

		for (int i = 1; i <= mx; i++){
			rest = min(rest, fn(i));
		}

		fout << "Case #" << q + 1 << ": " << rest << endl;
	}

	

	fout.close();

	return 0;
}