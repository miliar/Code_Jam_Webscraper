#include <iostream>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

typedef unsigned long long ull;
typedef vector<int> vi;
#define SZ(v) (int)(v.size())
#define INF 2000000000

long double C,F,X;

long double cost(int farms){
	long double tot = 0;
	for(int i=0; i<farms; i++){
		tot+=C/(2+F*i);
	}
	return tot + X / (2+F*farms);
}

void solve(int testcase){
	
	cin >> C >> F >> X;
	cout << setprecision(7) << fixed;
	long double best = INF;
	int last=0;
	for(int farms = 1; ;){
		long double res = cost(farms);
		if(cost(farms-1)>res) ;
		else break;
		last = farms;
		if(last==0)farms++;
		else farms+=100;
	}
	for(int farms = last; ; farms++){
		long double res = cost(farms);
		if(res < best){
			best = res;
		} else{
			cout << best << endl;
			break;
		}
	}
	
	

	
	

}

int main() {
	int testcases;
	cin >> testcases;
	for(int i=1; i<=testcases; i++){
		printf("Case #%d: ",i);
		solve(i);
	}
	return 0;
}

