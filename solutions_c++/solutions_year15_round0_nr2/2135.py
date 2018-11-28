#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<queue>
#include<vector>
#include <string>
#include <cmath>

#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define println(X) printf("%d\n",(X))
#define PB push_back
#define MP make_pair
using namespace std;
vector<int> numbers;


bool can(int time){
	for (int numSpecial = 0; numSpecial < time; numSpecial++){
		int M = time - numSpecial;
		int needed = 0;
		for (int i = (int)numbers.size() - 1; i >= 0; i--){
			needed += ceil(numbers[i] * 1.0 / M) - 1;
			if (needed > numSpecial){
				break;
			}
		}
		if (needed <= numSpecial){
			return true;
		}
	}
	return false;
}
int main(){
	freopen("ihop.in", "r", stdin);
	freopen("ihop.out", "w", stdout);
	DRI(T);
	for (int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		DRI(D);
		numbers.clear();
		//numbers.push_back(0);
		for (int i = 0; i < D; i++){
			DRI(k); numbers.push_back(k);
		}
		sort(numbers.begin(), numbers.end());
		//do a binary search
		int lo = 0;
		int hi = 1001;
		while (hi - lo > 1){
			int mid = (hi + lo) / 2;
			if (can(mid)){
				hi = mid;
			}
			else{
				lo = mid;
			}
		}
		cout << hi << "\n";
	}
	return 0;
}