//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define N 100010
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)
#define MOD 1000002013 

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

int		data[N][3],n,m;
LL		in[N*2],out[N*2];
int		xx[N*2] , xcnt;
int		main(){
	int cas , tt = 0;
	scanf("%d", &cas );
	while ( cas -- ){
		scanf("%d%d", &n, &m );
		xcnt = 0;
		LL	ans = 0 , now = 0;
		Rep(i,m) {
			scanf("%d%d%d", &data[i][0] ,&data[i][1] , &data[i][2] );
			xx[xcnt++] = data[i][0];
			xx[xcnt++] = data[i][1];
			if ( data[i][0] == data[i][1] )  continue;
			int L = data[i][1] - data[i][0];
			LL g = n+n-L+1 , h = L;
			if ( g%2 == 0 ) g /= 2; else h /= 2;
			g %= MOD , h %= MOD;
			ans += g*h%MOD*data[i][2]%MOD;
			ans %= MOD;
		}
		sort( xx , xx+xcnt );
		xcnt = unique(xx,xx+xcnt) - xx;
		Rep(i,m){
			in[ lower_bound(xx,xx+xcnt,data[i][0])-xx ] += data[i][2];
			out[ lower_bound(xx,xx+xcnt,data[i][1])-xx ] += data[i][2];
		}
		for(int i = 0; i<xcnt; i++){
			int j = i;
			while ( out[i] ){
				for( ; in[j] == 0; j--);
				LL num = min(out[i],in[j]);
				out[i] -= num , in[j] -= num;
				if ( i == j ) continue;
				int L = xx[i]-xx[j];
				LL g = n+n-L+1 , h = L;
				if ( g%2 == 0 ) g /= 2; else h /= 2;
				g %= MOD , h %= MOD;
				num %= MOD;
				now += g*h%MOD*num%MOD;
				now %= MOD;
			}
		}
		ans -= now;
		ans %= MOD;
		ans += MOD;
		ans %= MOD;
		printf("Case #%d: %lld\n" , ++tt , ans );
	}
	return 0;
}
