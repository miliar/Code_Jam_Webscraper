#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
#define INF 0x7f7f7f7f

using namespace std;

int v[10001],next[10001];

int main(){
	int T;
	int e,r,n;
	long long ans;
freopen("B-small-attempt2.in","r",stdin);
freopen("B-small-attempt2.out","w",stdout);
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas ++){
		scanf("%d %d %d",&e,&r,&n);
		ans = 0;
		for(int i = 0; i < n; i ++){
			scanf("%d",&v[i]);
		}
		bool flag = false;
		for(int i = 0; i < n; i ++){
			flag = false;
			int j;
			for(j = i + 1; j < n; j ++){
				if(v[i] < v[j]){
					flag = true;
					break;
				}
			}
			if(flag) next[i] = j;
			else next[i] = -1;
		}
		int nowe = e;
		long long regaine;
		for(int i = 0; i < n; i ++){
			regaine = (long long)r * (next[i] - i);
			long long usee = e - regaine;
			if(usee < 0 || next[i] == -1)  usee = 0;
			if(usee > nowe){
				nowe += r;
				if(nowe > e){ 
					nowe = e;
					continue;
				}
				
				
			}
			
					ans += (long long)v[i] * (nowe - usee);
					nowe = usee + r;
				

		}
		printf("Case #%d: %lld\n",cas,ans);

	}
	return 0;
}