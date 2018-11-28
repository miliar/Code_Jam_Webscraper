#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <queue>


using namespace std;


int T,N;
int X;
vector<int> a;
vector<int> use;
int cas;

void solve()
{
	int cnt=0;
	for( int i = N-1; i >= 0; i-- ){
		if( use[i] == 1 )continue;
		use[i] = 1;
		for( int j = i-1; j >= 0; j-- ){
			if( use[j] == 0 && a[i]+a[j] <= X ){
				use[j] = 1;break;
			}
		}
		cnt++;
	}
	printf("Case #%d: %d\n",cas,cnt);
}

int main()
{
	scanf(" %d",&T);
	for( cas = 1; cas <= T; cas++ ){
		scanf(" %d %d",&N,&X);
		a.resize(N);
		use.resize(N);
		fill(use.begin(),use.end(),0);
		for( int i = 0; i < N; i++ )
			scanf(" %d",&a[i]);
		sort(a.begin(),a.end());

		solve();
	}

	return 0;
}