#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
#define maxn 1009
#define PS system("pause");
using namespace std;
int n,L;
char s[maxn],ans1[maxn],ans2[maxn];
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int tt,cot=1;
	scanf("%d",&tt);
	while(tt--){
		cin>>n>>L;
		bool ok=1;
		for(int i=1;i<=n+1;i++){
			scanf("%s",s);
			if(i<=n){
				int cnt=0;
				for(int j=0;j<L;j++){
					if(s[j]=='1')
						cnt++;
				}
				if(cnt==L){
					ok=0;
				}
			}
		}
		if(!ok){
			printf("Case #%d: IMPOSSIBLE\n",cot++);
			continue;
		}
		int tot=0;
		for(int i=0;i<L;i++){
			ans1[tot++]='?';
			ans1[tot++]='0';
		}
		ans1[tot++]='\0';
		tot=0;
		ans2[tot++]='0';
		for(int i=1;i<=L-1;i++){
			ans2[tot++]='1';
			ans2[tot++]='0';
		}
		ans2[tot++]='\0';
		printf("Case #%d: %s %s\n",cot++,ans1,ans2);
	}
	return 0;
}