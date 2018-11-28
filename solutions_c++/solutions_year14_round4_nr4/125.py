#include<stdio.h>
#include<algorithm>
using namespace std;
char str[100][100];
int ret;
int num;
struct Trie{
	int next[26];
	Trie(){
		for(int i=0;i<26;i++)next[i]=-1;
	}
};
Trie pool[100000];
int use[100];
int m,n;
void dfs(int a){
	if(a==m){
		int val=0;
		for(int i=0;i<n;i++){
			int count=0;
			int sz=1;
			pool[0]=Trie();
			for(int j=0;j<m;j++){
				if(use[j]==i){
					count++;
					int at=0;
					for(int k=0;str[j][k];k++){
						if(~pool[at].next[str[j][k]-'A'])at=pool[at].next[str[j][k]-'A'];
						else{
							pool[at].next[str[j][k]-'A']=sz;
							at=sz;
							pool[sz++]=Trie();
						}
					}
				}
			}
			if(count==0)return;
			val+=sz;
		}
		if(ret<val){
			ret=val;
			num=1;
		}else if(ret==val)num++;
		return ;
	}
	for(int i=0;i<n;i++){
		use[a]=i;
		dfs(a+1);
	}
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d%d",&m,&n);
		for(int i=0;i<m;i++)scanf("%s",str[i]);
		ret=0;
		num=0;
		dfs(0);
		//for(int i=1;i<=n;i++)num/=i;
		printf("Case #%d: %d %d\n",t+1,ret,num);
	}
}