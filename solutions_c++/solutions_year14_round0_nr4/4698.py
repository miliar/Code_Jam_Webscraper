// 4.Deceitful War.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include<vector>
using namespace std;

int _tmain(int argc, _TCHAR* argv[]){
	int t, size, x, y, naomiIt, kenIt;
	cin>>t;
	for(int i = 0; i < t; ++i){
		cin>>size;
		vector<double> naomi = vector<double>(size);
		vector<double> ken = vector<double>(size);
		for(int j = 0; j < size; ++j)
			cin>>naomi[j];
		for(int j = 0; j < size; ++j)
			cin>>ken[j];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		//Deceitful War
		x=0;
		naomiIt=kenIt=0;
		while(naomiIt < size && kenIt < size){
			if(naomi[naomiIt] > ken[kenIt]){
				++x;
				++kenIt;
			}
			++naomiIt;
		}
		//War
		y=0;
		naomiIt=kenIt=0;
		while(naomiIt < size && kenIt < size){
			if(naomi[naomiIt] < ken[kenIt])
				++naomiIt;
			else
				++y;
			++kenIt;
		}
		cout << "Case #" << i+1 << ": " << x << " " << y << endl;
	}
}