#include<bits/stdc++.h>
using namespace std;
#define eb emplace_back
#define pb push_back
#define mp make_pair
const int md=1e9+7;
const int inf=1e9;
const int maxn=123456;
int T,n,m,nq,nk,x;
int ans;
char s[maxn];
int q[maxn];
void task(){
	scanf("%s",s+1);
	n=strlen(s+1);
	int k,t=0;
	ans=0;
	for(int i=1;i<=n;i++){
		if(s[i]=='C') k=1;
		else k=2;
		if(t>0 && q[t]==k){
			ans+=10;
			t--;
		}else{
			q[++t]=k;
			
		}
	}
	ans+=t/2*5;
	printf("%d\n",ans);
}
int main(){		
	scanf("%d",&T);
	for (int t=1;t<=T;t++) {printf("Case #%d: ",t);task();}
	
}

