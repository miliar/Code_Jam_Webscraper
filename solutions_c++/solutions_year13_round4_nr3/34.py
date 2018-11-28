#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=2001;
int a[maxn],b[maxn];
int n;
int ans[maxn];
int cnt[maxn];
vector<int> edge[maxn];


void init(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++){
		scanf("%d",&a[i]);
	}
	for (int i=1;i<=n;i++){
		scanf("%d",&b[i]);
	}
	memset(cnt,0,sizeof(cnt));
	memset(ans,0,sizeof(ans));
	for (int i=1;i<=n;i++){
		edge[i].clear();
	}
	return;
}

void buildgraph(){
	for (int i=2;i<=n;i++){
		int last=-1;
		for (int j=i-1;j>=-1;j--){
			if (a[i]==a[j]+1){
				last=j;
				break;
			}
		}
		if (last!=-1){
			edge[i].push_back(last);
			cnt[last]++;
		}
		for (int j=1;j<i;j++){
			if (j==last){
				continue;
			}
			if (a[i]<a[j]+1){
				edge[j].push_back(i);
				cnt[i]++;
			}
		}
	}
	for (int i=1;i<n;i++){
		int last=-1;
		for (int j=i+1;j<=n;j++){
			if (b[i]==b[j]+1){
				last=j;
				break;
			}
		}
		if (last!=-1){
			edge[i].push_back(last);
			cnt[last]++;
		}
		for (int j=i+1;j<=n;j++){
			if (j==last){
				continue;
			}
			if (b[i]<b[j]+1){
				edge[j].push_back(i);
				cnt[i]++;
			}
		}
	}
	return;
}

void calc(){
	buildgraph();
	for (int i=n;i>0;i--){
		int cur=-1;
		for (int j=n;j>=1;j--){
			if (ans[j]!=0){
				continue;
			}
			if (cnt[j]!=0){
				continue;
			}
			cur=j;
			break;
		}
		ans[cur]=i;
		for (int j=0;j<edge[cur].size();j++){
			cnt[edge[cur][j]]--;
		}
	}
	for (int i=1;i<=n;i++){
		printf(" %d",ans[i]);
	}
	printf("\n");
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d:",i);
		calc();
	}
	return 0;
}
