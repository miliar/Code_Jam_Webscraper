#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>

typedef long long ll;
typedef long double ld;

using namespace std;

#define rep(a,b,c) for(int a=b;a<=c;++a)
#define per(a,b,c) for(int a=b;a>=c;--a)
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define PII pair<int,int>
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

map<pair<char,char>,char> mult;
char s[11111];
int TT,l,x,len,ok;
char cur;

char work(int l,int r){
	cur='1';
	rep(i,l,r)	cur=mult[mp(cur,s[l])];	
	return	cur;
}

int main(){
	mult[mp('1','1')]='1';mult[mp('1','i')]='i';mult[mp('1','j')]='j';mult[mp('1','k')]='k';
	mult[mp('i','1')]='i';mult[mp('i','i')]='1';mult[mp('i','j')]='k';mult[mp('i','k')]='j';
	mult[mp('j','1')]='j';mult[mp('j','i')]='k';mult[mp('j','j')]='1';mult[mp('j','k')]='i';
	mult[mp('k','1')]='k';mult[mp('k','i')]='j';mult[mp('k','j')]='i';mult[mp('k','k')]='1';
	scanf("%d",&TT);
	rep(T,1,TT){
		scanf("%d%d",&l,&x);
		gets(s);
		rep(i,1,x-1)	rep(j,0,l-1)	s[i*l+j]=s[j];
		len=l*x;ok=0;
		rep(i,0,len-1)
			if	(work(0,i)=='i' && ok==0)
				rep(j,i+1,len-1)
					if	(work(i+1,j)=='j' && work(j+1,len-1)=='k'){
						ok=1;
						break;
					}
		printf("Case #%d: ");
		if	(ok)	puts("YES");
		else	puts("NO");
	}
	return	0;
}

