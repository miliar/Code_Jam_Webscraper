#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>
using namespace std;

int first[4];
int second[4];
//int i, j;
void fillFirst();
void fillSecond();
void answer();

void go() {
	fillFirst();
	fillSecond();
	answer();

}

void answer(){
	int count = 0;
	int answer = 0;
	for(int i = 0; i <= 3; i++){
		for(int j = 0; j <= 3; j++){//can be improved but fuck off!!
			if(first[i] == second[j]){
				answer = first[i];
				count ++;
				break;
			}
		}
	}
	if(count == 0){
		cout << "Volunteer cheated!";
	} else if(count == 1){
		cout << answer;
	} else {
		cout << "Bad magician!";
	}
}

void fillFirst(){
	int k, m;
	cin >> k;
	for(int p = 1; p < k; p++){
		cin >> m; cin >> m; cin >> m; cin >> m;
	}

	for(int p = 1; p <= 4; p++){
		cin >> m;
		first[p - 1] = m;
	}

	for (int p = k; p <= 3; p++){
		cin >> m; cin >> m; cin >> m; cin >> m;
	}
}

void fillSecond(){
	int k, m;
	cin >> k;
	for(int p = 1; p < k; p++){
		cin >> m; cin >> m; cin >> m; cin >> m;
	}

	for(int p = 1; p <= 4; p++){
		cin >> m;
		second[p - 1] = m;
	}

	for (int p = k; p <= 3; p++){
		cin >> m; cin >> m; cin >> m; cin >> m;
	}
}

int main() { freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
cout << fixed << setprecision(12);

int testn;
cin >> testn;
for (int testc = 1; testc <= testn; testc++) {
	cout << "Case #" << testc << ": ";
	go();
	cout << '\n';
}
int i = 0;
}
