#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

char s[105][105];
string t[105];
int a[105][105];

int main() {
	int T,n,i,j;
	freopen("1.in","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&T);
	for(int tc=1;tc<=T;tc++) {
		scanf("%d",&n);
		for(i=1;i<=n;i++) {
			scanf("%s",s[i]);
			t[i].clear();
			int len=strlen(s[i]),c=0;
			for(j=0;j<len;j++) {
				t[i].push_back(s[i][j]);
				a[i][c]=1;
				while(j+1<len&&s[i][j+1]==s[i][j]) a[i][c]++,j++;
				c++;
			}
		}
		for(i=1;i<=n;i++) if(t[i]!=t[1]) break;
		if(i<=n) {
			printf("Case #%d: Fegla Won\n",tc);
			continue;
		}
		int ans=0;
		int len=t[1].size();
		for(j=0;j<len;j++) {
			int tmp=1000;
			for(i=1;i<=n;i++) {
				int t=a[i][j],sum=0;
				for(int k=1;k<=n;k++) {
					sum+=abs(t-a[k][j]);
				}
				tmp=min(tmp,sum);
			}
			ans+=tmp;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}
		

				


			
		
		

