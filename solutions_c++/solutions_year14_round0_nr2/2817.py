#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <utility>
#include <bitset>
using namespace std;

int GCD (int a, int b ) {
	if ( a==0 ) return b;
	return GCD ( b%a, a );
}

#define CetakInt(J) printf("Cetak %d\n",J);
#define CetakChar(J) printf("%c\n",J);
#define sf scanf
#define pf printf
#define FOR(a,b,c) for(int a = b; a<=c ; a++)
#define FOR1(a,b,c) for(int a = b; a<c; a++)

typedef long long int int64;

bool dsc (int i,int j) { 
	return (i>j); 
}

int main(){
	double C; //untuk tambah range
 	double F; //range
	double X; //finalnya bro
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; ++i) {
		double total = 0.00000000;
		cin >> C >> F >> X;
		for (double j = 2.00000000; ; j+=F) {
			double belifarm = C/j;
			double belisetelahfarm = X/(j+F);
			double belitanpafarm = X/j;
			if (belifarm + belisetelahfarm < belitanpafarm) {
				total+=belifarm;
			} else {
				total+=belitanpafarm;
				break;
			}
		}
		printf("Case #%d: %0.7f\n",i,total);
	}
	return 0;
}