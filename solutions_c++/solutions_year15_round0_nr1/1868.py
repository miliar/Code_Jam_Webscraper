#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;
int ntest;
int l;
string s;
int a[1100];

void solve(int test){
	printf("Case #%d: ",test+1);
	cin>> l; l++;
	cin >> s;
	for(int i=0; i<l; i++){
		a[i] = s[i]-'0';
	}
	int cur = a[0];
	int res=0;
	for(int j=1; j<l; j++){
		if( cur < j ){
			res += j-cur;
			cur = j;
		}
		cur += a[j];
	}
	printf("%d\n",res);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);
	for(int t=0; t<ntest; t++){
		solve(t);
	}
	return 0;
}
