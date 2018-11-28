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
#define INF 1000000
#define MOD 1000000007  
#define f first
#define s second
#define EPS 1e-9
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
//#define DFS_WHITE -1
//#define DFS_BLACK 0

ii arr[255][255];

int main(){
	Rd;
	Wr;

	arr[1][1] 	= ii('i', 1); 
	arr[1]['i'] = ii('i', 1); 
	arr[1]['j'] = ii('j', 1); 
	arr[1]['k'] = ii('k', 1); 

	arr['i'][1] 	= ii('i', 1); 
	arr['i']['i'] 	= ii( 1 , -1); 
	arr['i']['j'] 	= ii('k', 1);
	arr['i']['k'] 	= ii('j', -1);

	arr['j'][1] 	= ii('j', 1); 
	arr['j']['i'] 	= ii('k', -1); 
	arr['j']['j'] 	= ii( 1 , -1);
	arr['j']['k'] 	= ii('i', 1);

	arr['k'][1] 	= ii('k', 1); 
	arr['k']['i'] 	= ii('j', 1); 
	arr['k']['j'] 	= ii('i', -1);
	arr['k']['k'] 	= ii( 1 , -1);

	int T, n, x, L, c;
	string str;
	sc(T);
	loop(t,0,T){
		printf("Case #%d: ", t+1);
		sc(L); sc(x); 
		cin >> str;
		c = 0;
		ii p;
		p.f = 1;
		p.s = 1;
		while(x-- > 0){
			loop(i,0,L){
				int sign = p.s;
				p = arr[p.f][str[i]];
				p.s *= sign;

				if(p.f == 'i' && p.s == 1 && c == 0) {
					p.f = 1;
					p.s = 1;
					c++;
				}
				else if(p.f == 'j' && p.s == 1 && c == 1) {
					p.f = 1;
					p.s = 1;
					c++;
				}
			}
		}
		if(p.f == 'k' && p.s == 1 && c == 2) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}