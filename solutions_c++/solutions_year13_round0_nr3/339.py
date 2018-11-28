#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<

typedef long long ll;

ll pd[111][11][2][2];
char N[2][111];
bool oi[2][111];
int oi0, oi1;
ll go(int x, int y, int z, int w, int c, int u) { // cuidado
	if( y > 9 ) return 0;
	if( x == 0 ) {
		if( c == 1 && oi0 ) return 0;
		if( c == 2 && oi1 ) return 0;
		if( w == 0 ) return 2*y < 10; // par
		else return 2*y-u < 10; // impar
	}
	
	if( !c && ~pd[x][y][z][w] ) return pd[x][y][z][w];
	x--;
	
	ll r = 0;
	if( c == 1 ) {
		fr(i,z,N[0][x]) r += go(x, y+i*i, 0, w, 0, i*i);
		if( N[0][x] >= z ) r += go(x,y+N[0][x]*N[0][x],0,w,1, N[0][x]*N[0][x]);
	} else if( c == 2 ) {
		fr(i,z,N[1][x]) r += go(x, y+i*i, 0, w, 0, i*i);
		if( N[1][x] >= z ) r += go(x,y+N[1][x]*N[1][x],0,w,2, N[1][x]*N[1][x]);
	} else {
		fr(i,z,10) r += go(x, y+i*i, 0, w, 0, i*i);
	}
	if( !c ) pd[x+1][y][z][w] = r;
	return r;
}

char a[111], b[111];

/*
ll ok[1<<20];
int k = 0;

bool pal(ll x) {
	char tmp[20];
	sprintf(tmp,"%lld", x);
	int n = strlen(tmp);
	fr(i,0,n) if( tmp[i] != tmp[n-1-i] ) return false;
	return true;
}
//*/

struct BI {
	vector<int> x;
	BI(const char * s) {
		int n = strlen(s);
		if( n == 0 && s[0] == '0' ) return;
		x.resize(n);
		fr(i,0,n) x[i] = s[n-i-1]-'0';
	}
	BI(vector<int> y): x(y) {}
	BI quad() {
		int n = x.size();
		if( !n ) return *this;
		vector<int> z(n*2-1, 0);
		fr(i,0,n) fr(j,0,n) z[i+j] += x[i]*x[j];
		fr(i,0,2*n-2) z[i+1] += z[i]/10, z[i]%=10;
		while( z[z.size()-1] >= 10 ) {
			int k = z[z.size()-1]/10;
			z[z.size()-1]%=10;
			z.push_back(k);
		}
		return BI(z);
	}
	BI met() const {
		int n = x.size();
		vector<int> z(n, 0);
		fr(i,0,n) {
			z[i] += x[i]/2;
			if( i && x[i]%2 ) z[i-1] += 5;
		}
		if( !z[n-1] ) z.pop_back();
		return BI(z);
	}
	BI menosum() const {
		int n = x.size();
		vector<int> z(x);
		z[0]--;
		fr(i,0,n) if( z[i] < 0 ) z[i] += 10, z[i+1]--;
		if( !z[n-1] ) z.pop_back();
		return BI(z);
	}
	BI operator+(const BI & y) const {
		int n = max(x.size(), y.x.size());
		vector<int> z(n);
		fr(i,0,n) z[i] = (i<x.size()?x[i]:0) + (i<y.x.size()?y.x[i]:0);
		fr(i,1,n) z[i] += z[i-1]/10, z[i-1]%=10;
		while( z[z.size()-1] >= 10 ) {
			int k = z[z.size()-1]/10;
			z[z.size()-1]%=10;
			z.push_back(k);
		}
		return BI(z);
	}
	bool operator<(const BI & y) const {
		if( x.size() < y.x.size() ) return 1;
		if( y.x.size() < x.size() ) return 0;
		vector<int> t1 = x, t2 = y.x;
		reverse(t1.begin(),t1.end());
		reverse(t2.begin(),t2.end());
		return t1 < t2;
	}
	void print(char * s) {
		int n = x.size();
		fr(i,0,n) s[i] = x[n-i-1]+'0';
		s[n] = 0;
		if( !n ) s[0] = '0', s[1] = 0;
	}
};

void doit(char * x) {
	BI a("0"), b(x), c(x);
	while( a < b ) {
		BI d = (a+b+BI("1")).met();
		if( c < d.quad() ) b = d.menosum();
		else a = d;
	}
	a.print(x);
}

void doit2(char * x) {
	BI a("0"), b(x), c(x);
	
	while( a < b ) {
		BI d = (a+b).met();
		if( d.quad() < c ) a = d+BI("1");
		else b = d;
	}
	a.print(x);
}


int main() {
	/*
	fr(i,1,(100<<20)) {
		if( pal(i) && pal(i*(ll)i) ) ok[k++] = i*(ll)i, db( i _ ok[k-1] );
	}
	//db(k);
	//fr(i,0,k) db( ok[i] );
	return 0;
	//*/
	memset(pd,-1,sizeof pd);
	int t, caso = 1;
	scanf("%d", &t);
	while( t-- ) {
		scanf("%s%s", a, b);
		//memset(a,'9',sizeof a);
		//memset(b,'9',sizeof b);
		//a[1] = b[100] = 0;
		//doit2(a);
		doit(b);
		printf("Case #%d: ", caso++);
		int na = strlen(a);
		a[na-1]--;
		for( int i = na-1 ; i >= 0 ; --i ) {
			if( a[i] < '0' ) a[i-1]--, a[i] += 10;
		}
		fr(ii,0,na) {
			if( a[ii] != '0' ) {
				fr(i,ii,na) a[i-ii] = a[i];
				na -= ii;
				a[na] = 0;
				break;
			}
		}
		//db(a);
		doit(a);
		na = strlen(a);
		//db(a _ b);
		
		int nb = strlen(b);
		reverse(a,a+na);
		reverse(b,b+nb);
		oi0 = 0;
		for( int i = na-1 ; i >= na/2 ; --i ) if( a[i] > a[na-1-i] ) {
			oi[0][i] = 1;
			oi0 = 1;
		} else oi[0][i] = 0;
		for( int i = 0 ; i < (na+1)/2 ; ++i ) N[0][i] = a[i+na/2]-'0', oi[0][i] = oi[0][i+na/2];
		
		oi1 = 0;
		for( int i = nb-1 ; i >= nb/2 ; --i ) if( b[i] > b[nb-1-i] ) {
			oi[1][i] = 1;
			oi1 = 1;
		} else oi[1][i] = 0;
		for( int i = 0 ; i < (nb+1)/2 ; ++i ) N[1][i] = b[i+nb/2]-'0', oi[1][i] = oi[1][i+nb/2];
		int nna = na, nnb = nb;
		na = (na+1)/2;
		nb = (nb+1)/2;
		
		//fr(i,0,na) printf("%d", N[0][i]); puts("");
		//fr(i,0,nb) printf("%d", N[1][i]); puts("");
		
		
		
		ll r = 0;
		fr(i,1,nnb) r += go((i+1)/2,0,1,i%2,0,0);
		r += go(nb,0,1,nnb%2,2,0);
		//db(r);
		fr(i,1,nna) r -= go((i+1)/2,0,1,i%2,0,0);
		r -= go(na,0,1,nna%2,1,0);
		
		printf("%lld\n", r);
	}
	return 0;
}

