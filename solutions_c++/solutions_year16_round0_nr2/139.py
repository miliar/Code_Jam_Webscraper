#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;
char s[1000];
int a[1000];
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);

	int tail=0;
	int tt,ri=0;
	scanf("%d",&tt);
	while(tt--){
		scanf(" %s",s);
		int len=strlen(s);
		tail=0;
		for(int i=0;i<len;++i){
			if(i==len-1||s[i]!=s[i+1]){
				if(s[i]=='+')
					a[tail++]=1;
				else
					a[tail++]=0;
			}
		}
		int ans=tail-1;
		if(a[tail-1]==0)
			ans++;
		printf("Case #%d: %d\n",++ri,ans);
	}
	return 0;
}
