#include <iostream>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef long long ll;
map<string, int> mp;
map<string, int>::iterator it;
int ID, L, R;
char s[100000];
int idx(){
	it=mp.find(s);
	if(it!=mp.end())
		return it->second;
	return mp[s]=ID++;
}
int E[100000];
int F[100000];
int n;
vector<vector<int> > v(n);
int res;
void calc(int i, int c){
	if (i == n){
		res=min(res,c);
		return;
	}
	for (int t = 0; t<2; ++t){
		if (i == 0 && t)
			continue;
		if(i==1 && !t)
			continue;
		int add=0;
		for(int k=0;k<v[i].size();++k){
			int now=0;
			if(t==0)
				now=++E[v[i][k]]==1;
			else
				now=++F[v[i][k]]==1;
			if (now && E[v[i][k]] && F[v[i][k]])
				++add;
		}
		calc(i+1,c+add);
		for (int k = 0; k<v[i].size(); ++k)
			if (t == 0)
				--E[v[i][k]];
			else
				--F[v[i][k]];
	}
}
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Z = 1; Z <= T; ++Z){
		printf("Case #%d: ", Z);
		ID=0;
		mp.clear();
		scanf("%d",&n);
		gets(s);
		v.clear();
		v.resize(n);
		for(int i=0;i<n;++i){
			gets(s);
			stringstream CIN(s);
			while(CIN>>s)
				v[i].push_back(idx());
		}
		memset(E, 0, sizeof(E));
		memset(F, 0, sizeof(F));
		res=1<<29;
		calc(0, 0);
		printf("%d\n", res);
	}
	return 0;
}