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

#include <iostream>       // std::cout
#include <string>         // std::string
//#include <bitset>         // std::bitset
#include <vector>

using namespace std;

int A, B, K;

void answer();


void answer(){
	int answer = 0;

	cin >> A;
	cin >> B;
	cin >> K;
	for(int i = 0; i < A; i++){
		for(int j = 0; j < B; j++){
			int m = i&j;
			if(m < K){
				answer ++;
			}
		}
	}
		cout << answer;
	}


int main() { freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//cout << fixed << setprecision(12);

	int testn;
	cin >> testn;
	for (int testc = 1; testc <= testn; testc++) {
		cout << "Case #" << testc << ": ";
		answer();
		cout << '\n';
	}
}
