#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <cstring>
using namespace std;
int ans[1010];
bool check(int x) {
	static char tmp[20],tmp2[20];
	sprintf(tmp,"%d",x);
	strcpy(tmp2,tmp);
	reverse(tmp2,tmp2+strlen(tmp));
	return !strcmp(tmp,tmp2);
}
int main() {
	int _,a,b,ca(0); cin>>_;
	for(int i(0);i*i<1010;++i)
		if(check(i) && check(i*i))
			ans[i*i] = 1;
	partial_sum(ans,ans+1010,ans);
	while(_--) {
		cin>>a>>b;
		printf("Case #%d: %d\n",++ca,ans[b]-ans[a-1]);
	}
	return 0;
}
