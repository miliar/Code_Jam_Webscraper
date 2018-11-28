#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF 200000000
#define MOD 1000000007  
//#define f first
//#define s second
#define EPS 1e-9
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
//#define DFS_WHITE 0
//#define DFS_BLACK 1


int main(){
	Rd;
	Wr;
	int T, n;
	ll ans = 0, c = 0;
	string s;
	sc(T);
	loop(t,0,T){
		printf("Case #%d: ", t+1);
		sc(n);
		n++;
		cin >> s;
		c = s[0]-'0';
		ans = 0;
		loop(j,1,n){
			if(j > c && s[j] > '0'){
				ans += (j-c);
				c = j;
			}
			c += (s[j]-'0');
		}
		printf("%lld\n", ans);
	}
	return 0;
}

