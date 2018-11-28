//============================================================================
// Name        : helloWorld.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#define ull unsigned long long
#define ll long long

#define REP(i,a,n) for(int (i)=a;(i)<(int)(n);(i)++)
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

	int T,t = 0;
	cin >> T;

	while(t < T){
		int Smax;
		cin >> Smax;
		string shies;
		cin >> shies;

		int totalReq = 0;
		int curTotal = 0;
		int temp = 0;
		while(temp < Smax+1){
			int forThisReq = temp-curTotal-totalReq;
			if(forThisReq <=0 ){

			}else{
				totalReq += forThisReq;
			}
			curTotal = curTotal + (0 + shies[temp] - '0');
			temp++;
		}
		cout << "Case #" << t << ": " << totalReq << endl;
		t++;
	}

}
