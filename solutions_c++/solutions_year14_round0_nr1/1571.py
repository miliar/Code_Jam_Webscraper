#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#define X first
#define Y second
#define fo(i,n) for(int i=0;i<n;i++)
#define fr(i,n) for(int i=1;i<=n;i++)
#define pb push_back

using namespace std;

typedef long long ll;

const int mod=(int)1e9+7;

int T,cas,vis[20];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		int x;
		memset(vis,0,sizeof vis);
		scanf("%d",&x);
		fr(i,4){
			int y;
			fr(j,4){
				scanf("%d",&y);
				if(x==i) vis[y]++;
			}
		}
		scanf("%d",&x);
		fr(i,4){
			int y;
			fr(j,4){
				scanf("%d",&y);
				if(x==i) vis[y]++;
			}
		}
		int flag=0,ans;
		fr(i,16)
			if(vis[i]==2)
				flag++,ans=i;
		printf("Case #%d: ",++cas);
		if(!flag) printf("Volunteer cheated!\n");
		else if(flag>1) printf("Bad magician!\n");
		else printf("%d\n",ans);
	}
	return 0;
}

