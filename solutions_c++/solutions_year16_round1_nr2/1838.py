#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
map<int,int> mp;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,tmp,n;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d",&n);
		mp.clear();
		for(int i=0;i<2*n-1;i++){
			for(int j=0;j<n;j++){
				scanf("%d",&tmp);
				mp[tmp]++;
			}
		}
		map<int,int>::iterator it;
		printf("Case #%d: ",cas);
		for(it=mp.begin();it!=mp.end();it++){
			if(it->second%2) printf("%d ",it->first);
		}
		puts("");
	}
	return 0;
}
