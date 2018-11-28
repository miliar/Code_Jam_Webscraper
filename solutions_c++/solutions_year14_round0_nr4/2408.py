#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define PRINTCASE printf("Case #%d: ",case_n++)
#define PRINTCASE_ printf("Case #%d:\n",case_n++)
#define RD(a) scanf("%d", &a)
#define RDD(a, b) scanf("%d%d", &a, &b)

int N;
vector<double> a(1000, 0), b(1000, 0);

int go1(){
	int ia = 0, ib = 0, cnt = N;
	for(; ia < N; ++ia){
		if(a[ia] < b[ib]){
			--cnt;
		}else{
			++ib;
		}
	}
	return cnt;
}

int go2(){
	int ia = 0, ib = 0, cnt = 0;
	for(; ia < N; ++ia){
		while(ib < N && b[ib] < a[ia]){
			++cnt;
			++ib;
		}
		if(ib < N) ++ib;
	}
	return cnt;
}

int main(){
	freopen("large-in.txt", "r", stdin);
	freopen("large-out.txt", "w", stdout);
	CASET{
		cin >> N;
		for(int i = 0; i < N; ++i) scanf("%lf", &a[i]);
		for(int i = 0; i < N; ++i) scanf("%lf", &b[i]);
		sort(a.begin(), a.begin() + N);
		sort(b.begin(), b.begin() + N);
		PRINTCASE;
		cout << go1() << " " << go2() << endl;
	}
	return 0;
}