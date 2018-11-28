#include <bits/stdc++.h>
#define FOR(i, from, to) for (int i = (from) ; i < to ; i++)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define SYNC ios_base::sync_with_stdio(0);
#define ri(i) scanf("%d",&i)
#define rii(i,j) scanf("%d%d",&i,&j)
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define EPS 1e-9
#define PI 3.1415926535897932384626

using namespace std;

typedef long long ll;

typedef pair<int, int> ii;

typedef vector<int> vi;
typedef vector<ii> vii;

int gcd(int a, int b){ return b ? gcd(b, a % b) : a; }
int mcm(int a, int b){ return a * b / gcd(a, b); }
int sq(int a) { return a*a; }
int pot(int a, int b){ return b ? sq(pot(a, b >> 1))*(b & 1 ? a : 1) : 1; }
//int roofLog2(int n) { int r = 1; for ( ; r < n ; r <<= 1); return r; }

bool d[10]={};
int c=0;
void m(long long n){
	ll a=n;
	while(a>0){
		if(!d[a%10]){
			d[a%10]=true;
			c++;
		}
		a/=10;
	}
}
int main(){
	int T;cin>>T;
	FOR(i,1,T+1){
		c=0;
		ms(d,0);
		ll N;cin>>N;
		//cout<<N<<endl;
		if(N==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else{
			ll M=N;
			while(c!=10){
				m(N);
				N+=M;
				//cout<<N<<" "<<c<<endl;
			}
			cout<<"Case #"<<i<<": "<<N-M<<endl;
		}
	}


	
}