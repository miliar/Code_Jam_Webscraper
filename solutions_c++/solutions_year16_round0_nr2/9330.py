#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

char str[20];
bool vis[1<<11];
int n;

int bfs(int mask){
	queue<int> q;
	q.push(mask);
	vis[mask]=1;

	int level=0;
	while(!q.empty()){
		int sz=q.size();
		while(sz--){

			int cur=q.front();
			q.pop();

			if(__builtin_popcount(cur)==n)return level;

			for(int i=0;i<n;++i){
				int tmp=cur;

				for(int j=i,ii=0;j>=0;--j,++ii){
					if(!(cur&(1<<j)))tmp|=(1<<ii);
					else{
						if(tmp&(1<<ii))tmp^=(1<<ii);
					}
				}

				if(!vis[tmp])q.push(tmp), vis[tmp]=1;
			}
		}
		++level;
	}

	return -1;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;scanf("%d",&T);
	for(int cs=1;cs<=T;++cs){

		scanf("%s",str);
		n=strlen(str);

		int mask=0;
		for(int i=0;i<n;++i)
			if(str[i]=='+')mask|=(1<<i);


		mem(vis,0);
		printf("Case #%d: %d\n",cs,bfs(mask));
	}
	return 0;
}
