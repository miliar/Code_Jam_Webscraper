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

int n,ct,len,flag;
vector<string> v,rep;
vector<int> c;
string s;

int fun()
{
    int i,l,f[30];
    for(i=0;i<30;i++) f[i]=0;
    l = s.size();
    f[s[0]-97] = 1;
    for(i=1;i<l;i++)
    {
                    if(s[i]==s[i-1])continue;
                    if( f[s[i]-97] == 0 ) {f[s[i]-97]=1; continue;}
                    return 0;
    }
    return 1;
}

                    
int main()
{
    int t,k,i;
    scan(t);
    for(k=1;k<=t;k++)
    {
                     scan(n);
                     v.clear();
                     for(i=0;i<n;i++)
                     {
                                     s.clear();
                                     cin>>s;
                                     v.push_back(s);
                     }
                     sort(v.begin(),v.end());
                     rep.clear();
                     c.clear();
                     rep.push_back(v[0]);
                     c.push_back(1);
                     ct = 1;
                     for(i=1;i<n;i++)
                     {
                                     if(v[i]==rep[ct-1])
                                     {
                                                      c[ct-1]++;
                                     }
                                     else
                                     {
                                         rep.push_back(v[i]);
                                         c.push_back(1);
                                         ct++;
                                     }
                     }
                     ct = 0;
                     s.clear();
                     for(i=0;i<n;i++)
                     s+=v[i];
                     if(fun()) ct++;
                     while( next_permutation(v.begin() , v.end()) )
                     {
                                                      s.clear();
                                                      for(i=0;i<n;i++)
                                                      s += v[i];
                                                      if(fun()) ct++;
                     }
                     int temp;
                     temp = c.size();
                     for(i=0;i<temp;i++) ct *= c[i];
                     printf("Case #%d: %d\n",k,ct);
    }
    return 0;
}
                     
