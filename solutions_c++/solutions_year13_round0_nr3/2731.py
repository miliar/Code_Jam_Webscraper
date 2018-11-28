// C

#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

long long a[1000001],qqq;
bool check[1000001];

bool pal(long long x) {
	long long i,k=1,cnt=0;
	char tmp[20];
	for ( i=1; i<=100000000000000; i*=10 ) {
		if ( x/i==0 ) break;
		else tmp[cnt++]=(x/i)%10 + '0';
	}
	
	long long q=0, p=cnt-1;
	while(q<p) {
		if ( tmp[q]!=tmp[p] ) return false;
		q++; p--;
	}
	return true;
}

int main() {
	long long t,i,j,n,m,Z=1,res;
	for ( qqq=1; qqq<=1000000; qqq++ ) {
		a[qqq]=qqq*qqq;
		if ( pal(qqq*qqq) && pal(qqq) ) check[qqq]=true;
		else check[qqq]=false;
	}

	FILE *fo=fopen("C-small-attempt0.in","r");
	freopen("output.txt","w",stdout);

	fscanf(fo,"%lld",&t);
	while(t--){
		res=0;
		fscanf(fo,"%lld %lld",&n,&m);
		for ( i=1; i<=1000000; i++ ) {
			if ( n<=a[i] && a[i]<=m ) {
				if ( check[i]==true ) res++;
			}
			else if ( a[i]>m ) break;
		}


		printf("Case #%lld: %lld\n",Z++,res);
	}
	return 0;
}