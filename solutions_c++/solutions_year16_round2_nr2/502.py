//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define LL long long int
#define inf 1000000000000000000LL;
char c[30],j[30];
int n;
LL best;
LL bc,bj;
void dfs(int now,LL cc,LL jj){
	if(cc-jj>best) return ;
	if(now==n){
		if(best>abs(cc-jj)){
			best=abs(cc-jj);
			bc=cc;
			bj=jj;
		}else if(best==abs(cc-jj)){
			if(cc<bc){
				bc=cc; bj=jj;
			}else if(cc==bc){
				if(jj<bj){
					bc=cc; bj=jj;
				}
			}
		}
		return ;
	}
	int i,x;
	if(c[now]=='?'&&j[now]=='?'){
		dfs(now+1,cc*10+0,jj*10+0);
		if(cc>=jj){
			dfs(now+1,cc*10+0,jj*10+1);
			dfs(now+1,cc*10+0,jj*10+9);
		}
		if(cc<=jj){
			dfs(now+1,cc*10+1,jj*10+0);
			dfs(now+1,cc*10+9,jj*10+0);
		}
	}else if(c[now]=='?'){
		int d=(int)(j[now]-'0');
		dfs(now+1,cc*10+d,jj*10+d);
		if(cc<jj){
			dfs(now+1,cc*10+9,jj*10+d);
		}else if(cc>jj){
			dfs(now+1,cc*10+0,jj*10+d);
		}else{
			if(d!=0) dfs(now+1,cc*10+d-1,jj*10+d);
			if(d!=9) dfs(now+1,cc*10+d+1,jj*10+d);
		}
	}else if(j[now]=='?'){
		int d=(int)(c[now]-'0');
		dfs(now+1,cc*10+d,jj*10+d);
		if(cc<jj){
			dfs(now+1,cc*10+d,jj*10+0);
		}else if(cc>jj){
			dfs(now+1,cc*10+d,jj*10+9);
		}else{
			if(d!=0) dfs(now+1,cc*10+d,jj*10+d-1);
			if(d!=9) dfs(now+1,cc*10+d,jj*10+d+1);
		}
	}else{
		dfs(now+1,cc*10+(int)(c[now]-'0'),jj*10+(int)(j[now]-'0'));
	}
}
int main(void){
    int t,hh;
    scanf("%d",&t);
    for(hh=1;hh<=t;hh++){
		scanf("%s %s",c,j);
		n=strlen(c);
		best=inf;
		dfs(0,0,0);
		//printf("%lld %lld\n",bc,bj);
		printf("Case #%d: ",hh);
		int oc[20],oj[20];
		int i;
		for(i=n-1;i>=0;i--){
			oc[i]=bc%10;
			bc/=10;
		}
		for(i=n-1;i>=0;i--){
			oj[i]=bj%10;
			bj/=10;
		}
		for(i=0;i<n;i++) printf("%c",(char)(oc[i]+'0'));
		printf(" ");
		for(i=0;i<n;i++) printf("%c",(char)(oj[i]+'0'));
		printf("\n");
	}
    return 0;
}
