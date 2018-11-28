#include <cstdio>
#include <string.h>
#include <algorithm>
using namespace std;

int n,m,used[1000],ans,mmn;
char s[1000][500];


int f(int a){
	//printf("%d\n",a);
	int ret = 0;
	for(int i=0;i<n;i++){
		if(used[i] != a) continue;
		ret += strlen(s[i]);
		int dis=0;
		for(int j=i-1,k;j>=0;j--){
			if(used[j] != a) continue;
			for(k=0;s[i][k] !=0 && s[i][k] == s[j][k];k++);
			if(k>dis)dis = k;
		}
		ret -= dis;
	}
	
	if(ret == 0) return -1;
	return ret;
}

void dfs(int nod){
	if(nod == n){
		
		int rmp = m;
		for(int i=0;i<m;i++)
			rmp += f(i);
		if(rmp==mmn) ans++;
		if(rmp>mmn) mmn=rmp,ans=1;
		
		return;
	}
	for(int i=0;i<m;i++){
		used[nod] = i;
		dfs(nod+1);
	}
}

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
	
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++){
			scanf("%s",s[i]);
			used[i]=-1;
		}
		
		mmn=0,ans=0;
		dfs(0);
        
        printf("Case #%d: %d %d\n", tt, mmn, ans);
    }
    return 0;
}

