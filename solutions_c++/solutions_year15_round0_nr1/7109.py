#include<cstdio>
#include<iostream>
using namespace std;
int n;
char str[1010];
int main(){
	//freopen("a.in","r",stdin);
	//freopen("a3.out","w",stdout);
	int T,Case=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		scanf("%s",str);
		int now=0,ans=0;
		for(int i=0;i<=n;i++){
			int k=str[i]-'0';
			if(k){
				if(now<i){
					ans+=i-now;
					now+=i-now;
					now+=k;
				}else now+=k;
			}
		}
		printf("Case #%d: %d\n",++Case,ans);
	}
	return 0;
}
