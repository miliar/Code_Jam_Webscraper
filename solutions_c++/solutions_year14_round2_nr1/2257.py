#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
using namespace std;
const int MAX =100+5;
int n;
int vis[MAX];
int ind[MAX];

int main(){
	int testcase;
	scanf("%d", &testcase);
	int cnt=0;
	while(testcase--){
		scanf("%d", &n);
		int ans=0;
		memset(vis,-1,sizeof(vis));
		memset(ind,0,sizeof(ind));
		bool ok = true;
		int c=0;
		char tmp[MAX][MAX];
		scanf("%s", tmp[0]);
		int now_cnt=1;
		vis[0] = tmp[0][0] - 'a';
		for(int i=1;i<strlen(tmp[0]);++i){
			if(tmp[0][i]-'a' != vis[now_cnt-1])	
				vis[now_cnt++] = tmp[0][i] - 'a';
		}
		int next[MAX];
		memset(next,-2,sizeof(next));
		for(int i=1;i<n;++i){
			scanf("%s", tmp[i]);
			int new_cnt=1;
			if(ok==true){
				next[0] = tmp[i][0] -'a';
				for(int j=1;j<strlen(tmp[i]);++j){
					if(tmp[i][j]-'a' != next[new_cnt-1])
					next[new_cnt++]=tmp[i][j]-'a';
				}	
			}
			int ma = now_cnt > new_cnt ? now_cnt:new_cnt;
			for(int w=0;w<ma;++w){
				if(next[w] != vis[w]){
					ok=false;
					break;
				}
			}
		}
		if(ok==false){
			printf("Case #%d: Fegla Won\n", ++cnt);
			continue;
		}

		int num[MAX];
		//memset(num,0,sizeof(num));
		while(ind[0] != strlen(tmp[0])){
			int tot=0;
			memset(num,0,sizeof(num));
			for(int i=0;i<n;++i){
				for(int j=ind[i];j<strlen(tmp[i]);++j){
					num[i]++;
					ind[i]++;
					if((tmp[i][j]-'a') != (tmp[i][j+1]-'a')){
						tot+=num[i];
						break;
					}	
				}
			}
			int mid = tot/n;
			for(int i=0;i<n;++i){
				ans+=abs(num[i]-mid);
			}
		}

		printf("Case #%d: %d\n", ++cnt, ans);
	}
	return 0;
}
