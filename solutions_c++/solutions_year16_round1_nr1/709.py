#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#define LL long long
using namespace std;
char ans[5000];
char s[5000];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	int tt,ri=0;
	scanf("%d",&tt);
	while(tt--){
		int l,r;
		l=r=1500;
		scanf(" %s",s);
		int len=strlen(s);
		for(int i=0;i<len;++i){
			if(l==r||s[i]>=ans[l])
				ans[--l]=s[i];
			else
				ans[r++]=s[i];
		}
		printf("Case #%d: ",++ri);
		for(int i=l;i<r;++i)
			printf("%c",ans[i]);
		puts("");
	}
	return 0;
}
