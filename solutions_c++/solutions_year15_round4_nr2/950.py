# include <bits/stdc++.h>
# define ll long long
# define pll pair < ll, ll >
# define fs first 
# define se second
# define mp make_pair
# define pb push_back
# define rep(i, n) for( ll (i) = 0; (i) < (n); (i)++)
# define REP(i, n) for( ll (i) = 1; (i) <= (n); (i)++)
# define wl(i) while((i)--)
# define vec vector < ll >
# define ma map < ll, ll >
# define sf(i) scanf("%lld",&(i))
# define pr(i) printf("%lld ",(i))
# define prn(i) printf("%lld\n",(i))
# define cpr(i) cout<<(i)<<" "
# define cprn(i) cout<<(i)<<endl
# define csf(i) cin>>(i)
# define srt(v) sort( v.begin(), v.end() )
# define srtc(v, x) sort( v.begin(), v.end(), x)
# define srtr(v) sort( v.begin(), v.end(), greater< ll >())
# define mod 1000000007
# define MAX_PRIME 0
# define SEGMENT_MAX 0

using namespace std;

bool compare( const ll &a, const ll &b ){
	return a < b ;
}

int main(){
	freopen("read.txt", "r", stdin);
	freopen("write.txt", "w", stdout);
	ll t;
	sf(t);
	REP(kr, t){
		printf("Case #%lld: ",kr);
		ll n; sf(n);
		double x, y;
		scanf("%lf%lf",&x, &y);
		double a[n][2];
		rep(i, n){
			scanf("%lf%lf",&a[i][0], &a[i][1]);
		}
		if( ( n > 1 ) && ( a[1][1] == a[0][1]) ){
			n = 1;
			a[0][0] += a[1][0];
		}
		if( n == 1){
			if( y == a[0][1] ){
				printf("%lf\n", x/a[0][0]);
			}
			else
				printf("IMPOSSIBLE\n");
		}
		else{
			if( a[0][1] < a[1][1] ){
				swap(a[0][0], a[1][0]);
				swap(a[0][1], a[1][1]);
			}
			if( y <= a[0][1] && a[1][1] <= y ){
				double v0 = ( x*( y - a[1][1])/(a[0][1] - a[1][1]));
			//	cprn(v0);
				printf("%lf\n", max( v0/a[0][0] , ( x - v0)/a[1][0]));
			}
			else{
				printf("IMPOSSIBLE\n");
			}
		}
	}
	return 0;
}