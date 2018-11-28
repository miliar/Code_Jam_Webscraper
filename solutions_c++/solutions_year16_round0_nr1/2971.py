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

int N;
bool vis[10];

bool go (int now){
	while (now){
		vis[ now%10 ] = 1;
		now /= 10;
	}
	for (int i=0;i<10;i++){
		if (!vis[i])	return false;
	}
	return true;
}

int main (){
//	freopen ("F:\\C++\\A-large.in", "r", stdin);
//	freopen ("F:\\C++\\A-large.out", "w", stdout);
	
	int T; scanf ("%d",&T);
	int cas = 1;
	while (T--){
		scanf ("%d", &N);
		if (N == 0){
			printf ("Case #%d: INSOMNIA\n", cas++);
		}
		else{
			memset (vis, 0, sizeof(vis));
			int now = N;
			for (;;){
				if (go (now))
					break;
				now = now + N;
			}
			printf ("Case #%d: %d\n", cas++, now);
		}
	}
	return 0;
}