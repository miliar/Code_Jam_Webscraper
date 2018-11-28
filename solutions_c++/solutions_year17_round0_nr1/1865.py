#include<bits/stdc++.h>


using namespace std;

const int maxn = 1010;

int n,k,cas;

char st[maxn];
int A[maxn];

void Work(){
	for(int i=1;i<=n;i++)if(st[i]=='-')A[i]=1;else A[i]=0;
	int ans=0;
	for(int i=1;i+k-1<=n;i++){
		if(A[i]){
			ans++;
			for(int j=i;j<=i+k-1;j++)A[j]^=1;
		}
	}
	printf("Case #%d: ",++cas);
	for(int i=1;i<=n;i++)if(A[i]){
		puts("IMPOSSIBLE");
		return;
	}
	printf("%d\n",ans);
}

void Init(){
	scanf("%s",st+1);
	n=strlen(st+1);
	scanf("%d",&k);
}

int main(){
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int T;
	scanf("%d",&T);
	while(T--)
		Init(),
		Work();
	return 0;
}
