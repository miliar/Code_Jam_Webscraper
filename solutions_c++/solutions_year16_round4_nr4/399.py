#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <cassert>
#include <vector>
#define all(x) x.begin() , x.end()
#define fi first
#define se second
#define pb push_back
#define umax( x , y ) x = max( x , (y) )
#define umin( x , y ) x = min( x , (y) )
#define For( i , a ) for(int i=1;i<=a;i++)
#define ort (b+s)/2
#define y2 asrwjaelkf
#define y1 asseopirwjaelkf
#define set multiset

using namespace std;

inline int read() {
	int res = 0 ;int neg ;
	while(true){char ch = getchar();if(ch>='0' && ch<='9' || ch=='-'){if(ch=='-') neg = -1;else neg = 1 , res = ch-'0';break;} }
	while(true){char ch = getchar();if(ch>='0' && ch<='9') res*=10 , res+=ch-'0';else break;}
	return res*neg;
}


typedef long long Lint;
typedef long double db;
typedef pair<int,int> ii;
typedef pair<db,db> dd;
typedef pair<ii,int> iii;
typedef pair<ii,ii> i4;

const int maxn = 2020;
const int maxm = 1000020;
const int MOd = 1e9 + 7;
const int K = 320;

int a;

//~ int used[210][120][120];
//~ db dn[210][120][120];
db dn[210][120];
char ar[50][50];
int b;
ii loc[maxn];
int used[5];
int used2[5];

int dfs( int n ) {
	if( n == a+1 ) {
		return 1;
	}
	int t = 0;
	for(int i=1;i<=a;i++)
		if( !used[i] ) {
			used[i] = 1;
			for(int j=1;j<=a;j++)
				if( !used2[j] && ar[i][j] == '1' ) {
					t = 1;
					used2[j] = 1;
					if( !dfs( n+1 ) ) {
						used[i] = used2[j] = 0;
						return 0;
					}
					used2[j] = 0;
				}
			used[i] = 0;
		}
	return t;
}

void solve() {
	
	scanf("%d",&a);
	int s = 0;
	for(int i=1;i<=a;i++) {
		scanf("%s",ar[i]+1);
		for(int j=1;j<=a;j++)
			if( ar[i][j] == '0' ) loc[++s] = ii( i, j );
	}
	//~ printf("asd %d\n",dfs( 1 ));
	//~ return ;
	int ans = s;
	
	for(int i=0;i<(1<<s);i++) {
		int t = 0;
		for(int j=0;j<s;j++)
			if( (1<<j)&i ) ar[loc[j+1].fi][loc[j+1].se] = '1', t++;
		memset( used, 0, sizeof( used ) );
		memset( used2, 0, sizeof( used2 ) );
		//~ if( i == 4 ) printf("%c %c\n%c %c\n",ar[1][1],ar[1][2],ar[2][1],ar[2][2]);
		if( dfs( 1 ) ) umin( ans, t );
		
		for(int j=0;j<s;j++)
			if( (1<<j)&i ) ar[loc[j+1].fi][loc[j+1].se] = '0';
	}
	printf("%d\n",ans);
}

int main() {
	
	int n;
	scanf("%d",&n);
	int cnt = 0;
	while( n-- ) {
		printf("Case #%d: ",++cnt);
		solve();
	}
	
	return 0;
}
