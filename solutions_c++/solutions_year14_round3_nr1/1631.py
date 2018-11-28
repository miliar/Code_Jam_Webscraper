#include<stdio.h>
#include<string>
#include<cstring>
#include<set>
#include<iostream>
#include<vector>
#include<math.h>
#include<stdlib.h>
#include<stdint.h>
#include<algorithm>
#include<map>

typedef long long LL;

using namespace std;

//#define MOD 1000000007
 
#define gx getchar
#define px putchar
#define ps putchar(' ')
#define pn putchar('\n')

//Scanning functions
void scan( int &n ) {	int sign = 1; n = 0;	char c = gx();	while( c < '0' || c > '9' ) {		if( c == '-' ) sign = -1;		c = gx();	}	while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();	n = n * sign;}
void lscan( LL &n ) {	int sign = 1; n = 0;	char c = gx();	while( c < '0' || c > '9' ) {		if( c == '-' ) sign = -1;		c = gx();	}	while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();	n = n * (LL)(sign);}
int sscan( char a[] ) {	char c = gx();	while(c==' ' || c=='\n') c=gx();	int i=0;	while(c!='\n')a[i++] = c,c=gx();	a[i]=0; return i;}
int wscan( char a[] ) {	char c = gx();	while(c==' ' || c=='\n') c=gx();	int i=0;	while(c!='\n' && c!=' ')a[i++] = c,c=gx();	a[i]=0; return i;}

//Printing functions
void print( int n ) {	if(n<0) {		n=-n;		px('-');	}	int i=10;	char o[10];	do {		o[--i] = (n%10) + '0'; n/=10;	}while(n);	do {		px(o[i]);	}while(++i<10);}
void lprint( LL n ) {	if(n<0LL) {		n=-n;		px('-');	}	int i=21;	char o[21];	do {		o[--i] = (n%10LL) + '0'; n/=10LL;	}while(n);	do {		px(o[i]);	}while(++i<21);}
void sprint( const char a[] ) {	const char *p=a;	while(*p)px(*p++);}

void twoscan( LL &a, LL &b ) {
	a=b=0LL;
	char c=gx();
	while(c<'0'||c>'9')c=gx();
	while(c>='0'&&c<='9')a=(a<<3)+(a<<1)+c-'0',c=gx();
	c = gx();
	while(c>='0'&&c<='9')b=(b<<3)+(b<<1)+c-'0',c=gx();
}

void reduce( LL &p, LL &q ) {
	LL m = min(p,q);
	LL rm = (LL)(sqrt(m)) + 1;
	for( LL i = 2; i < rm; ++i ) {
		while( (p%i == 0) && (q%i == 0) ) {
			p = p/i;
			q = q/i;
		}
	}
	if( q%p == 0 ) {
		q = q/p;
		p = 1;
	}
	if ( p%q == 0 ) {
		p = p/q;
		q = 1;
	}
}

int main() {
	int t, T;
	LL pa, qa;
	scan(T);
	for( t = 1; t <= T; ++t ) {
		twoscan(pa,qa);
		cout << "Case #" << t << ": ";
		reduce(pa,qa);
		if( ( 1LL<<(int)log2(qa) != qa ) ) cout << "impossible\n";
		else {
			double cur, act;
			act = (double)(pa) / (double)(qa);
			cur = 1.0/2.0;
			int i = 1;
			while( cur != 0.0 ) {
				if( cur <= act ) {
					cout << i << endl;
					break;
				}
				++i; cur = cur/2.0;
			}
		}
	}
	return 0;
}

