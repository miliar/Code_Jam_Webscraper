#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define INF (1<<29)
#define EPS (1e-10)
#define make_pair mp
#define pb push_bacck
#define FOR(i,a,b) for(int i=a; i<b; i++ )

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;

int dx[] = {0,1,0,-1}, dy[] = {1,0,-1,0};

int main(){
	int T;
	cin >> T;
	for( int t=1; t<T+1; t++ ){
		int a, b, k;
		cin >> a >> b >> k;
		int ans = 0;
		for( int i=0; i<a; i++ ){
			for( int j=0; j<b; j++ ){
				if( i < k && j < k ) ans++;
				else{
					if( (i & j) < k ) ans++;
				}
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
