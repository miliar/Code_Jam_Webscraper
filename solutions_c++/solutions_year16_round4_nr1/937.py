#include <bits/stdc++.h>
using namespace std;
int cnt[600];
char ss[5]="RPS";
string dfs(int level,int st){
	string ste="",s1,s2;
	if (level==0) {
		ste+=ss[st];
		return ste;
	}
		s1=dfs(level-1,st);
		s2=dfs(level-1,(st+2)%3);
		if (s1<s2) return s1+s2;
		return s2+s1;
}
		int n,r,p,s;
int main(){
	freopen("a.txt","r",stdin);
	freopen("aaout.txt","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d%d",&n,&r,&p,&s);
		printf("Case #%d: ", ++ca);

		string tmp=dfs(n,0);
		
		memset(cnt,0,sizeof cnt);
		for (int i=0;i<(1<<n);i++)
			cnt[tmp[i]]++;
		if (cnt['R']==r&&cnt['P']==p&&cnt['S']==s){
			printf("%s\n",tmp.c_str());
			continue;
		}
		tmp=dfs(n,1);
		
		memset(cnt,0,sizeof cnt);
		for (int i=0;i<(1<<n);i++)
			cnt[tmp[i]]++;
		if (cnt['R']==r&&cnt['P']==p&&cnt['S']==s){
			printf("%s\n",tmp.c_str());
			continue;
		}
		tmp=dfs(n,2);
		
		memset(cnt,0,sizeof cnt);
		for (int i=0;i<(1<<n);i++)
			cnt[tmp[i]]++;
		if (cnt['R']==r&&cnt['P']==p&&cnt['S']==s){
			printf("%s\n",tmp.c_str());
			continue;
		}
		puts("IMPOSSIBLE");
	}
	return 0;
}