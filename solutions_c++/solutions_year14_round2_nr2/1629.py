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

int main()
{
    int t,a,b,k,x,ct,i,j;
    scan(t);
    for(x=1;x<=t;x++)
    {
                     scan(a);
                     scan(b);
                     scan(k);
                     ct = 0;
                     for(i=0;i<a;i++)
                     {
                                      for(j=0;j<b;j++)
                                      {
                                                      if( (i&j) < k ) ct++;
                                      }
                     }
                     printf("Case #%d: %d\n",x,ct);
    }
    return 0;
}
