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
db ar[410];
int b;

void solve() {
	
	memset( dn, 0, sizeof( dn ) );
	//~ memset( used, 0, sizeof( used ) );
	
	scanf("%d %d",&a,&b);
	
	for(int i=1;i<=a;i++) {
		cin >> ar[i];
	}
	sort( ar+1, ar+1+a );
	for(int i=1;i<=a;i++) ar[a+i] = ar[i];
	db h = 0.0;
	for(int i=1;i<=a;i++) {
		memset( dn, 0, sizeof( dn ) );
		dn[0][0] = 1.0;
		for(int j=1;j<=b;j++) {
			for(int k=0;k<=b/2;k++) {
				dn[j][k] = (1-ar[i+j-1]) * dn[j-1][k];
				if( k ) dn[j][k] += ar[i+j-1] * dn[j-1][k-1];
				//~ printf("asd %d %d --> %Lf\n",j,k,dn[j][k]);
			}
		}
		umax( h, dn[b][b/2] );
		
	}
	
	//~ cout << h << endl;
	printf("%.12lf\n",double(h));
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
