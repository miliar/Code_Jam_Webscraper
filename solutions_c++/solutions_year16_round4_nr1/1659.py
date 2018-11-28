#include<cstdio>
#include<algorithm>

int n,r,p,s;
int a[1<<13];
int ans[1<<13];
int check(int k){
	if(k==1<<n){
		int n1=(1<<(n-1));
		for(int i=0;i<(1<<n);i++)ans[i]=a[i];
		while(n1){
			for(int i=0;i<n1;i++){
				if(ans[i*2]==ans[i*2+1])return 0;
				else if(ans[i*2]+ans[i*2+1]==1)ans[i]=0;
				else if(ans[i*2]+ans[i*2+1]==3)ans[i]=1;
				else if(ans[i*2]+ans[i*2+1]==2)ans[i]=2;
			}
			n1/=2;
		}
		return 1;
	}
	if(p){
		a[k]=0;
		p--;
		if(check(k+1))return 1;
		p++;
	}
	if(r){
		a[k]=1;
		r--;
		if(check(k+1))return 1;
		r++;
	}
	if(s){
		a[k]=2;
		s--;
		if(check(k+1))return 1;
		s++;
	}
	return 0;
}
int main(){
	freopen("inA","r",stdin);
	freopen("outA","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%d%d%d%d",&n,&r,&p,&s);
		if(check(0)==1){
			for(int i=0;i<(1<<n);i++){
				if(a[i]==0)printf("P");
				else if(a[i]==1)printf("R");
				else printf("S");
			}
			puts("");
			continue;
		}
		puts("IMPOSSIBLE");
	}
}
