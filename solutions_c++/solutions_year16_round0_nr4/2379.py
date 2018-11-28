#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <queue>
#include <math.h>
#define MP make_pair

using namespace std;
typedef long long LL;
typedef unsigned int uint;
typedef pair<int,int> pii;
const double pi = atan (1.0) * 4;

int K,C,S;

int main (){
//	freopen ("F:\\C++\\D-small-attempt0.in", "r", stdin);
//	freopen ("F:\\C++\\D-small-attempt0.out", "w", stdout);
	
	int T; scanf ("%d",&T);
	int cas = 1;
	while (T--){
		scanf ("%d%d%d",&K,&C,&S);
		printf ("Case #%d:",cas++);
		LL tmp = 1;
		for (int i=0;i<C-1;i++)
			tmp *= K;
		LL now = 0;
		for (int i=0;i<S;i++){
			printf (" %lld", now+1);
			now += tmp;
		}
		printf ("\n");
	}
	return 0;
}