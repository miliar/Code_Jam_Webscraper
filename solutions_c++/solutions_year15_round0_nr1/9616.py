#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<cstdlib>
#include<ctime>
#include<cmath>
using namespace std;
typedef long long LL;
#define N 10010

int n;
char s[N];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,t=1;
	scanf("%d",&T);
	while(T--){
		int ans=0,now=0;
		scanf("%d%s",&n,s);
		for(int i=0;i<=n;i++){
			if(s[i]=='0') continue;
			if(now<i){
				ans+=i-now;
				now=i;
			}
			now+=s[i]-'0';
		}
		printf("Case #%d: %d\n",t++,ans);
	}
	return 0;
}
