#include <iostream>
#include <time.h>
#include <vector>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <map>
#include <algorithm>
#include <bitset>
#include <queue>
#include <set>
#include <time.h>
#include <assert.h>
#include <unordered_map>
#if !ONLINE_JUDGE
#include "inc.h"
#endif
using namespace std;
typedef long long ll;

const int N = 100 + 10;
char s[N];
int n;
void flip(char *r){
	for(int i=0;r[i];++i)
		r[i]=r[i]=='+'?'-':'+';
	reverse(r,r+n);
}
int calc(char *r){
	int cnt=0;
	for(int i=1;r[i];++i)
		cnt+=r[i]!=r[i-1];
	cnt+=r[n-1]=='-';
	return cnt;
}

int main() {
#if !ONLINE_JUDGE
	freopen("aa.txt", "r", stdin);
	freopen("bb.txt", "w", stdout);
	decTime;
#endif

	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;++T){
		scanf("%s",s);
		n=strlen(s);
		int mn=calc(s);
		flip(s);
		mn=min(mn,1+calc(s));
		printf("Case #%d: %d\n",T,mn);
	}

#if !ONLINE_JUDGE
	//printTime;
#endif
	return 0;
}