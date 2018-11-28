#include<cstdio>
#include<string>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;
#define LL long long
vector <LL> v;
char str[50],str1[50];
bool check(char s[]) {
	int len = strlen(s);
	int tem = len/2 -1;
	for(int i = 0; i <= tem; i++) {
		if(s[i] != s[len - 1- i])
			return false;
	}
	return true;
}
void init() {
	for(LL i = 1; i <= 1000000; i++) {
		sprintf(str1,"%I64d",i);
		sprintf(str,"%I64d",i*i);
		if(check(str)&&check(str1))
			v.push_back(i*i);
	}
}
int find(LL k) {
	int l = 0,r = v.size(),mid;
	while(l <= r) {
		mid = (l+r) >> 1;
		if(v[mid] == k)
			return mid;
		if(v[mid] > k)
			r = mid - 1;
		else l = mid + 1;
	}
	return mid;
}
int main () {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	init();
	int T,n,m;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++) {
		scanf("%d%d",&n,&m);
		int ans = 0;
		for(int i = 0; i < v.size(); i++)
			if(v[i] >= n && v[i] <= m)
				ans++;
		printf("Case #%d: ",cas);
		printf("%d\n",ans);
	}
	return 0;
}