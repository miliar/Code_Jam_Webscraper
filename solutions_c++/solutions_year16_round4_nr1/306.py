#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <string>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define inf 1000000007
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define pfi pair<double,int>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 110
#define max3(a,b,c) max(max(a,b),c)
#define mod 754754

#define put PutInt
#define send Send
#define get GetInt
#define receive Receive

typedef long long ll;
using namespace std;

int n0;

string go(int f,int n,int r,int p,int s){

	if(n == 0){
		string ret;
		if(f == 0) ret = 'R';
		if(f == 1) ret = 'P';
		if(f == 2) ret = 'S';
		return ret;
	}

	string a1, a2;
	if(f == 0){
		a1 = go(0,n-1,r,p,s);
		a2 = go(2,n-1,r,p,s);
	}
	if(f == 1){
		a1 = go(1,n-1,r,p,s);
		a2 = go(0,n-1,r,p,s);
	}
	if(f == 2){
		a1 = go(2,n-1,r,p,s);
		a2 = go(1,n-1,r,p,s);
	}

	string u;
	if(a1 < a2)
		u = a1 + a2;
	else
		u = a2 + a1;

	if(n == n0){
		for(int i=0;i<u.size();i++){
			if(u[i] == 'R') r--;
			if(u[i] == 'P') p--;
			if(u[i] == 'S') s--;
		}
		if(r || p || s)
			return "z";
	}

	return u;

}

main(){

	int nt;
	scanf("%d",&nt);

	for(int t=1;t<=nt;t++){

		int n, r, p, s;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		n0 = n;

		string ans = "z";

		ans = min(ans,go(0,n,r,p,s));
		ans = min(ans,go(1,n,r,p,s));
		ans = min(ans,go(2,n,r,p,s));

		printf("Case #%d: ",t);
		if(ans == "z")
			printf("IMPOSSIBLE\n");
		else
			cout << ans << endl;

	}

}
