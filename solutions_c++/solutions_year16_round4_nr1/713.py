#include <bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(auto it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define ALL(G) (G).begin(),(G).end()

#if 1
	#define DEB printf
#else
	#define DEB(...)
#endif

typedef long long LL;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;
const int inft = 1000000009;
const int MOD = 1000000007;
const int MAXN = 1000006;
char win(char x, char y){
	 fru(i,2){
		  if(x=='P' && y=='S') return 'S';
		  if(x=='P' && y=='R') return 'P';
		  if(x=='S' && y=='R') return 'R';
		  swap(x,y);
	 }
	 assert(0);
}

bool ok(string a){
	 if(a.size()==1) return 1;
	 assert(__builtin_popcount(a.size())==1);
	 string b="";
	 fru(i,a.size()/2){
		  char x=a[2*i],y=a[2*i+1];
		  if(x==y) return 0;
		  b=b+win(x,y);
	 }
	 return ok(b);
}
string W[15][3];

string solve(){
	 int p,r,s,n;
	 scanf("%d%d%d%d",&n,&r,&p,&s);
	 string q="";
	 fru(i,3){
		  string S=W[n][i];
		  int rr=r,ss=s,pp=p;
		  tr(it,S) if(*it=='P') --pp;
		  tr(it,S) if(*it=='R') --rr;
		  tr(it,S) if(*it=='S') --ss;
		  if(pp==0 && rr==0 && ss==0 && (q=="" || q>S)) q=S;
	 }
	 if(q!="") return q;
	 return "IMPOSSIBLE";
}
string S="RPS";

int main(){
	fru(i,3) W[0][i]=S[i];
	for(int i=1;i<15;++i)fru(z,3){
		 string q="";
		 fru(x,3) fru(y,3) if(x!=y && win(S[x],S[y])==S[z]){
			  string t=W[i-1][x]+W[i-1][y];
			  if(q=="" || q>t) q=t;
		 }
		 W[i][z]=q;
	}
	int o;
	scanf("%d",&o);
	fru(oo,o){
		 printf("Case #%d: ",oo+1);
		 printf("%s\n",solve().c_str());		 
	}
    return 0;
}
