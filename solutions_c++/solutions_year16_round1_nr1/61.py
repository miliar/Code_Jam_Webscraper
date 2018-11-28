#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;++i)
#define per(i,a,b) for(int i=b-1;i>=a;--i)
#define set(a,b) memset(a,b,sizeof(a))
#define de(x) cout << #x << " = " << x << endl
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef double db;
typedef pair<int, int> pii;
typedef vector<int> vi;
const db pi = acos(-1.0), eps = 1e-8;
const int inf = ~0U >> 2 , mod = 1e9 + 7;
int Pow(int x, ll t){int r=1;for(;t;t>>=1,x=(ll)x*x%mod)if(t&1)r=(ll)r*x%mod;return r;}
int T;
char s[1010];

void setIO(){
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
}

void main2(){
	scanf("%s",s);
	int len = strlen(s);
	int first = 0;
	vector<char> a , b;
	rep(i,0,len) if(s[i] >= first) first = s[i] , a.pb(s[i]);
	else b.pb(s[i]);
	per(i,0,sz(a)) printf("%c",a[i]);
	rep(i,0,sz(b)) printf("%c",b[i]);
	printf("\n");
}

int main(){
	setIO();
	scanf("%d",&T);
	rep(i,1,T+1){
		printf("Case #%d: ",i);
		main2();
	}
	return 0;
}

