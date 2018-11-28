#include <bits/stdc++.h>
using namespace std;
#define de(x) cout << #x << " = " << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
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
const double pi = acos(-1.0), eps = 1e-8;
const int inf = ~0U >> 2 , P = 1e9 + 7;
int Pow(int x,ll t){int r=1;for(;t;t>>=1,x=(ll)x*x%P)if(t&1)r=(ll)r*x%P;return r;}
void setIO(){
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
}
int T;
char s[100000];
char st[101010];int _;
int wk(){
	scanf("%s",s);
	int len = strlen(s);
	_ = -1;
	rep(i,0,len){
		if(_ >= 0 && st[_] == s[i]) --_;
		else st[++_] = s[i];
	}
	return 5 * (len - (_+1)/2);
}

int main(){
	setIO();
	scanf("%d",&T);
	rep(i,1,T+1){
		printf("Case #%d: %d\n",i ,wk());
	}
	return 0;
}
