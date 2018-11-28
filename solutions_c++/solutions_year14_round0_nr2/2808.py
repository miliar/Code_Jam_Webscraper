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
    int t,k;
    double c,f,x,time,temp1,temp2,r;
    scan(t);
    for(k=1;k<=t;k++)
    {
                     cin>>c;
                     cin>>f;
                     cin>>x;
                     time = 0;
                     r = 2;
                     while(1)
                     {
                             temp1 = x/r;
                             temp2 = (c/r) + (x/(r+f));
                             if(temp1 < temp2) {time += x/r;break;}
                             time += c/r;
                             r += f;
                             //cout<<time<<endl;
                     }
                     printf("Case #%d: %.7lf\n",k,time);
    }
    return 0;
}
