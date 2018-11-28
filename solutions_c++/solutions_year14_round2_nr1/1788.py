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

vector<char>ab, bb;
vector<int>xb, yb;
string s;

int main() {
	int t, Tb, n;
	scan(Tb);
	int i, j, k;
	char e, f;
	bool flag;
	for( t = 1; t <= Tb; ++t ) {
		cout << "Case #" << t << ": ";
		cin >> n;
		s. reserve(n);
		flag = 0;
		ab.clear();
		bb.clear();
		xb.clear();
		yb.clear();
		cin >> s;
		for( j = 0; j < s.size(); ++j ) {
			e = s[j];
			k = 1;
			while( j < s.size() && s[j] == e ) {++j; ++k;}
			--j;
			ab.push_back(e);
			xb.push_back(k);
		}
		s.clear();
		cin >> s;
		for( j = 0; j < s.size(); ++j ) {
			e = s[j];
			k = 1;
			while( j < s.size() && s[j] == e ) {++j; ++k;}
			--j;
			bb.push_back(e);
			yb.push_back(k);
		}
		if( ab.size() != bb.size() ) {
			flag = 1;
		}
		else {
			for( j = 0; j < ab.size(); ++j ) {
				if( ab[j] != bb[j] ) {
					flag = 1; break;
				}
			}
			if( flag == 0 ) {
				LL sum = 0LL;
				for( i = 0; i < xb.size(); ++i ) {
					sum += (abs)(xb[i]-yb[i]);
				}
				cout << sum << endl;
			}
		}
		if(flag) {
			cout << "Fegla Won\n";
			continue;
		}
	}
	return 0;
}

