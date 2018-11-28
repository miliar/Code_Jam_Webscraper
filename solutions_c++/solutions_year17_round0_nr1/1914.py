/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-08
*/
#include<bits/stdc++.h>
using namespace std;
char buf[1111];
int ans,k,len;
int main() {
	int T;scanf("%d",&T);for(int _=1;_<=T;++_) {
		printf("Case #%d: ",_);
		ans=0;scanf("%s",buf);scanf("%d",&k);len=strlen(buf);
		for(int i=0;i<len;++i) {
			if(buf[i]=='-') {
				++ans;
				if(i+k>len) {
					puts("IMPOSSIBLE");goto nx;
				}
				for(int j=i;j<i+k;++j)buf[j]=buf[j]=='+'?'-':'+';
			}
		}
		printf("%d\n",ans);
	nx:;
	}
}