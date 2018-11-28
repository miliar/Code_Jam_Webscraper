#include<bits/stdc++.h>
#include<map>
#define M 2000000
using namespace std;
int E[M] , F[M];
map<int,int> mp;
vector<int> res;
vector<int> ans;
int tc = 0;
int T;
int m;
int ss;
int n;
main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	while(T > 0){
		ss = 0;
		tc++;
		res.clear();
		ans.clear();
		mp.clear();
		m = 0;
		scanf("%d",&n);
		for(int i = 1 ; i <= n ; i++){
			scanf("%d",&E[i]);
			mp[E[i]] = i;
		}
		for(int i = 1 ; i <= n ; i++){
			scanf("%d",&F[i]);
			ss+=F[i];
		}
		while(ss % 2 == 0){
			m++;
			ss/=2;
		}
		res.push_back(0);
		F[1]--;
		int ptr = 1;
		for(int i = 1 ; i <= m ; i++){
			while(F[ptr] == 0) ptr++;
			ans.push_back(E[ptr]);
			for(int j = 0 ; j < res.size() ; j++)	F[mp[res[j] + E[ptr]]]--;
			int x = res.size();
			for(int j = 0 ; j < x ; j++)	res.push_back(res[j] + E[ptr]);
		}
		printf("Case #%d: ",tc);
		for(int i = 0 ; i < ans.size() ; i++)	printf("%d ",ans[i]);
		printf("\n");
		T--;
	}	
}
