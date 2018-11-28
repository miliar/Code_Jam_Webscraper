#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
using namespace std;

#define rep(i,n) for (int i=1;i<=(n);++i)
#define rep2(i,x,y) for (int i=(x);i<=(y);++i)
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VII;


bool f[13][4096][4096];
VII l,l2;

void init(){
	memset(f,false,sizeof(f));
	f[0][1][0]=f[0][0][1]=f[0][0][0]=true;
	l.pb(mp(1,0));
	l.pb(mp(0,1));
	l.pb(mp(0,0));
	rep(i,12) rep2(r,0,(1<<(i-1))) rep2(p,0,(1<<(i-1))){
		if (f[i-1][r][p])		
		{
			int s=(1<<(i-1))-r-p;			
			f[i][r+p][p+s]=true;
		}
	}
}

struct fish{
	stack<string> r,p,s;
} b[13];
struct pear{
	int r,p,s;
} a[13];
string minimize(string a, int len){
	if (len == 1) return a;
	string x=minimize(a.substr(0,len/2),len/2);
	string y=minimize(a.substr(len/2,len/2),len/2);
	//cout << min(x+y,y+x) << " " << a << endl;
	return min(x+y,y+x);
}

void MAIN(){
	int n,r,p,s;
	scanf("%d%d%d%d",&n,&r,&p,&s);
	if (!f[n][r][p])
		cout << "IMPOSSIBLE" << endl;
	else{
		a[n].r=r; a[n].p=p; a[n].s=s;
		for (int i=n-1;i>=0;--i)
		{
			a[i].r=(1<<i)-a[i+1].p;
			a[i].p=(1<<i)-a[i+1].s;
			a[i].s=(1<<i)-a[i+1].r;
		}
		rep2(i,0,n){
			while (!b[i].r.empty()) b[i].r.pop();
			while (!b[i].p.empty()) b[i].p.pop();
			while (!b[i].s.empty()) b[i].s.pop();;
		}
		rep(i,a[n].r) b[n].r.push("R");		
		rep(i,a[n].p) b[n].p.push("P");
		rep(i,a[n].s) b[n].s.push("S");
		for(int i=n-1;i>=0;--i)
		{
			rep(j,a[i].r){
				b[i].r.push(b[i+1].r.top()+b[i+1].s.top());
				b[i+1].r.pop();
				b[i+1].s.pop();
			}
			rep(j,a[i].p){
				b[i].p.push(b[i+1].r.top()+b[i+1].p.top());
				b[i+1].r.pop();
				b[i+1].p.pop();
			}			
			rep(j,a[i].s){
				b[i].s.push(b[i+1].s.top()+b[i+1].p.top());
				b[i+1].s.pop();
				b[i+1].p.pop();
			}			
		}
		if (a[0].r==1)
			cout << minimize(b[0].r.top(),1<<n) << endl;
		else if (a[0].p==1)
			cout << minimize(b[0].p.top(),1<<n) << endl;
		else if (a[0].s==1)
			cout << minimize(b[0].s.top(),1<<n) << endl;
	}
}
int main() {
    freopen("d:\\oi\\gcj2\\A-large.in","r",stdin);
    freopen("d:\\oi\\gcj2\\A-large.out","w",stdout);
    init();
    int tt;
    scanf("%d",&tt);
    rep(i,tt)
    {
        printf("Case #%d: ",i);
        MAIN();
    }    
    return 0;
}