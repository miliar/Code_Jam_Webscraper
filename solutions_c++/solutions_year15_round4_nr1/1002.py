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
		ll r, c;
		sf(r); sf(c);
		char a[r][c + 1];
		rep(i, r){
			scanf("%s",a[i]);
		}
		int d[r]; int e[c];
		rep(i, r){
			ll counter = 0;
			rep(j, c){
				if( a[i][j] != '.')
					counter++;
			}
			d[i] = counter;
		}

		rep(i, c){
			ll counter = 0;
			rep(j, r){
				if( a[j][i] != '.')
					counter++;
			}
			e[i] = counter;
		}
		ll count = 0;
		ll flag = 0;
		rep(i, r){
			int j = 0;
			while( j < c  && a[i][j] == '.')j++;
			if(j == c)
				continue;
			if( j != c && ( d[i] > 1 || e[j] > 1) ){
				if( a[i][j] == '<')
					count++;
			}
			else{
				flag = 1;
			}
		}

		rep(i, r){
			int j = c - 1;
			while( j >= 0  && a[i][j] == '.')j--;
			if( j < 0 )
				continue;
			if( j >= 0 &&  (d[i] > 1 || e[j] > 1 )){
				if( a[i][j] == '>')
					count++;
			}
			else{
				flag = 1;
			}
		}

		rep(j, c){
			int i = 0;
			while( i < r  && a[i][j] == '.')i++;
			if( i == r)
				continue;
			if( i < r && ( d[i] > 1 || e[j] > 1 )){
				if( a[i][j] == '^')
					count++;
			}
			else{
				flag = 1;
			}
		}

		rep(j, c){
			int i =  r - 1;
			while( i >= 0  && a[i][j] == '.')i--;
			if( i < 0)
				continue;
			if( i >= 0 && ( d[i] > 1 || e[j] > 1 )){
				if( a[i][j] == 'v')
					count++;
			}
			else{
				flag = 1;
			}
		}
		if(flag){
			printf("IMPOSSIBLE\n");
		}
		else
			prn(count);
	}
	return 0;
}