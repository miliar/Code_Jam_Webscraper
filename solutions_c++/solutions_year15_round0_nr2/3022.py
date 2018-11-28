#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int s[2000],ans;
void dfs(int a, int b){
	if(b>=ans) return;
	if(a==0){
		ans=min(ans,b);
		return;
	}
	if(s[a]==0){
		dfs(a-1,b);
		return;
	}
	
	int q[2000];
	for(int i=1;i<=a;i++)
		q[i]=s[i];
	
	for(int i=0;i<a;i++)
		s[i]=s[i+1];
	dfs(a-1,b+1);
	for(int i=1;i<=a;i++)
		s[i]=q[i];

	if(a>1){
		s[a]--;
		s[a/2]++;
		s[(a+1)/2]++;
		dfs(a,b+1);
		for(int i=1;i<=a;i++)
			s[i]=q[i];
	}
	if(a>2){
		s[a]--;
		s[a/3]++;
		s[a/3+(a%3==1)]++;
		s[a/3+(a%3==2)]++;
		dfs(a,b+2);
		for(int i=1;i<=a;i++)
			s[i]=q[i];
	}
}
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
		int n,m=0;
		scanf("%d", &n);
		for(int i=0;i<n;i++){
			scanf("%d",&s[i]);
			m=max(m,s[i]);
		}
		
		ans = 1000;
		// dfs(10,0);
		
		for(int i=1;i<=m;i++){
			int a=0;
			for(int j=0;j<n;j++){
				a+=(s[j]-1)/i;
			}
			// printf("%d: %d\n", i, a);
			ans = min(a+i, ans);
		}
        
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}

