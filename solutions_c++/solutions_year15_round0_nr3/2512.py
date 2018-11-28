#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);++i)
#define fi first
#define se second
#define mp make_pair

typedef long long ll;
typedef pair<char, int> Data; //true...plus, false...minus

int TC;
int l;
ll x;
string s;

inline Data mul(Data a, Data b){
    char p=a.fi,q=b.fi;
    int f = a.se == b.se;
    if(p=='1')return mp(q,f);
    if(q=='1')return mp(p,f);
    if(p==q) return mp('1',f^1);
    if(p=='i'){
	if(q=='j') return mp('k',f);
	if(q=='k') return mp('j',f^1);
    }
    if(p=='j'){
	if(q=='i') return mp('k',f^1);
	if(q=='k') return mp('i',f);
    }
    if(p=='k'){
	if(q=='i') return mp('j',f);
	if(q=='j') return mp('i',f^1);
    }
}


Data le[10010],ri[10010],al;
bool ok;

int main(){
    scanf("%d", &TC);
    rep(tc,TC){
	ok=1;
    	printf("Case #%d: ", tc+1);
	scanf("%d %lld", &l, &x);

	static char in[10010];
	scanf("%s", in);
	s = in;
	string ns="";
	rep(i,x) ns += s;
	s = ns;
	l *= x;

	Data cur = mp('1',1);
	rep(i,l){
	    cur = mul(cur, mp(s[i],1));
	    le[i] = cur;
	}
	al = cur;
	cur = mp('1',1);
	for(int i=l-1;i>=0;--i){
	    cur = mul(mp(s[i],1), cur);
	    ri[i] = cur;
	}

	int pl=-1,pr=l+1;
	rep(i,l)if(le[i]==mp('i',1)){pl=i;break;}
	for(int i=l-1;i>=0;--i)if(ri[i]==mp('k',1)){pr=i;break;}
	if(pl==-1||pr==l+1||pl+1>=pr)ok=0;
	cur=mp('1',1);
	for(int i=pl+1;i<pr;++i){
	    cur = mul(cur, mp(s[i],1));
	}
	if(cur!=mp('j',1))ok=0;
	puts(ok?"YES":"NO");
    }
    return 0;
}

