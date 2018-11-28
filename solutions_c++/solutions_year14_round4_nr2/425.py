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


int T;
int cas;
int N;
vector<int> a;

void solve()
{
	int L = 0, R = N-1;
	int t;
	int ans=0;
	for( int x = 0; x < N; x++ ){
		t = L;
		for( int i = L; i <= R; i++ ){
			if( a[t] > a[i] )
				t = i;
		}
		int l = t-L;
		int r = R-t;
		if( l <= r ){
			L++;
			for( int i = t; i >= L; i-- )
				swap(a[i],a[i-1]);
		}else{
			R--;
			for( int i = t; i <= R; i++ )
				swap(a[i],a[i+1]);
		}
		ans += min(l,r);
	}
	printf("Case #%d: %d\n",cas,ans);
}

int main()
{
	scanf(" %d",&T);

	for(cas = 1; cas <= T; cas++ ){
		scanf(" %d",&N);
		a.resize(N);
		for( int i = 0; i < N; i++ )
			scanf(" %d",&a[i]);

		solve();
	}

	return 0;
}