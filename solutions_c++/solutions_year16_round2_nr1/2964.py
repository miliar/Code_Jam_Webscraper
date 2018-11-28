#define __cplusplus 201103L

#include <iostream>
#include <sstream>
#include <fstream>
#include <array>
#include <deque>
#include <forward_list>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <complex>
#include <iterator>
#include <memory>
#include <numeric>
#include <random>
#include <string>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <gmp.h>

using namespace std;


int compare(const void* a, const void* b) {
	if (*(char*)a > *(char*)b) {
		return 1;
	}
	else if (*(char*)a < *(char*)b) {
		return -1;
	}
	else
		return 0;
}

int main() {
	freopen("output.txt", "w", stdout);
	freopen("input.txt", "r", stdin);

	int T;
	string ss;
	char* s = (char*)malloc(10000);
	char* nso[10];
	char* ns[10];
	int a[10];
	int d;

	nso[0] = "ZERO";
	nso[1] = "ONE";
	nso[2] = "TWO";
	nso[3] = "THREE";
	nso[4] = "FOUR";
	nso[5] = "FIVE";
	nso[6] = "SIX";
	nso[7] = "SEVEN";
	nso[8] = "EIGHT";
	nso[9] = "NINE";

	a[0] = 0;
	a[1] = 6;
	a[2] = 7;
	a[3] = 2;
	a[4] = 5;
	a[5] = 4;
	a[6] = 3;
	a[7] = 8;
	a[8] = 9;
	a[9] = 1;

	for (int k = 0; k <= 9; k++){
		ns[k] = nso[k];
	}

	cin>>T;

	stringstream o("");


	for (int i = 0; i < T;i++) {
		if (i != 0)
			cout<<endl;
		cin>>ss;

		strcpy(s, ss.c_str());

		int len = strlen(s);

		cerr<<ss<<endl;

		cout<<"Case #"<<i+1<<": "<<"";
		int d = 0;
		for (int k = 0; k <= 9; k++) {
			d=a[k];
			int nslen = strlen(ns[d]);
			int nsi;
			for (nsi = 0; nsi < nslen; nsi++) {
				int found = 0;
				for (int j = 0; j < len; j++) {
					if (!found) {
						if (s[j] == ns[d][nsi]) {
							found = 1;
							s[j] = 'Y';
						}
					}
				}
				if (!found)
					break;
			}
			//cerr<<"d:"<<d<<";nsi:"<<nsi<<";nslen:"<<nslen<<";s:"<<s<<endl;

			if (nsi == nslen) {
				cerr<<d<<endl;
				//cout<<d;
				o<<d;
				k--;d=a[k];
				for (int j = 0; j < len; j++) {
					if (s[j] == 'Y') {
						s[j] = 'M';
					}
				}
			}
			else {
				for (int j = 0; j < len; j++) {
					if (s[j] == 'Y') {
						s[j] = ss.c_str()[j];
					}
				}
			}

		}

		for (int j = 0; j < len; j++) {
			if (s[j] != 'M') {
				cerr << "ERR:"<<s<<endl;
			}
		}
		//cerr << o<<endl;

		strcpy(s, o.str().c_str());
		qsort(s, strlen(s), 1, compare);
		cerr<<"o:"<<s<<endl;
		o.str("");
		o.clear();
		cout<<s;


	}




	return 0;
}

