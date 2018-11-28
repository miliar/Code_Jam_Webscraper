#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<ctime>
#include<cmath>
#include<set>
#define int64 long long
using namespace std;
int T,n,p,tim,ans,i,x;
multiset<int> S;
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d%d",&n,&p);
		for(i=1;i<=n;++i)scanf("%d",&x),S.insert(x);
		ans=0;
		while(!S.empty()){
			int v=*S.begin();
			S.erase(S.begin());
			ans++;
			if(S.empty())break;
			multiset<int> :: iterator it=S.lower_bound(p-v+1);
			if(it==S.begin())continue;
			it--;
			S.erase(it);
		}
		printf("Case #%d: %d\n",++tim,ans);
	}
}
