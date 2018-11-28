#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;
int ntest;
int n;
int a[1100];

int f(int x){
	int res = x;
	for(int i=0; i<n; i++){
		if( a[i] > x ) res += (a[i]-1)/x;
	}
	//cout << x << " " << res << endl;
	return res;
}

void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%d",&n);
	
	int mx=0;
	for(int i=0; i<n; i++){
		scanf("%d",&a[i]);
		mx = max(mx,a[i]);
	}
	
	int res=100000;
	for(int i=1; i<=mx; i++){
		res = min(res,f(i));
	}
	printf("%d\n",res);

}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);
	for(int t=0; t<ntest; t++){
		solve(t);
	}
	return 0;
}
