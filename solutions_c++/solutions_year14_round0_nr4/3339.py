/**
 *	Author : hkbharath
 *	Problem : https://code.google.com/codejam/contest/2974486/dashboard#s=p3
 *	Lang : C++
 */	

#include <bits/stdc++.h>

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define FOR(a,b,c) for(int a=b;a<=c;++a)
#define RFOR(a,b,c) for(int a=b;a>=c;--a)
#define LOOP(a) FOR(xx,1,a)
#define PB(b) push_back(b)
#define MP(a,b) make_pair(a,b)
#define MOD 1000000007
#define ALL(a) (a.begin(),a.end())
#define ARR(a,n) (a,a+n)

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

void solve(int tt){
	int n;
	scanf("%d",&n);
	double nomi[n+1],ken[n+1];
	FOR(i,0,n-1)scanf("%lf",nomi+i);
	FOR(i,0,n-1)scanf("%lf",ken+i);
	sort(nomi,nomi+n);
	sort(ken,ken+n);
	int war=0,j=0;
	FOR(i,0,n-1){
		while(j<n && ken[j]<nomi[i]){j++;war++;}
		j++;
		if(j>=n)break;
	}
	int dwar=0;
	j=n-1;
	RFOR(i,n-1,0){
		if(nomi[j]>ken[i]){j--;dwar++;}
	}
	printf("%d %d\n",dwar,war);
}

int main(){
	int t,it;
	scanf("%d",&t);
	for(it=1;it<=t;it++){
		printf("Case #%d: ",it);
		solve(it);
	}
}
