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
const int maxn=101;
vector<pair<int,int> > a[maxn];
bool row[maxn],clm[maxn];
int n,m;

void init(){
	for (int i=0;i<maxn;i++){
		a[i].clear();
	}
	scanf("%d%d",&n,&m);
	for (int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			int cur;
			scanf("%d",&cur);
			a[cur].push_back(make_pair(i,j));
		}
	}
	return;
}

bool check(){
	memset(row,0,sizeof(row));
	memset(clm,0,sizeof(clm));
	for (int i=maxn-1;i>=1;i--){
		for (int j=0;j<a[i].size();j++){
			if (row[a[i][j].first]&&clm[a[i][j].second]){
				return false;
			}
		}
		for (int j=0;j<a[i].size();j++){
			row[a[i][j].first]=true;
			clm[a[i][j].second]=true;
		}
	}
	return true;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		if (check()){
			puts("YES");
		} else {
			puts("NO");
		}
	}
	return 0;
}
