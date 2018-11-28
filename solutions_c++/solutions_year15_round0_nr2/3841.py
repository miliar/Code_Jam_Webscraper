#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <queue>

using namespace std;

int T,N;
int ar[1010];
priority_queue <int> q;

int main(){

	cin >> T;
	for( int z=1 ; z<=T ; z++ ){
		cin >> N;
		while( !q.empty() ) q.pop(); 
		for( int i=1 ; i<=N ; i++ )	scanf(" %d",&ar[i]);
		int ans=INT_MAX;
		for( int i=1 ; i<=1000 ; i++ ){
			int res=0;
			for( int j=1 ; j<=N ; j++ ) res+=(ar[j]-1)/i;
			ans=min( ans , res+i );
		}
		printf("Case #%d: %d\n",z,ans);
	}
}