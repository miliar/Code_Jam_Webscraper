#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=1010;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int a[maxn];
char s[maxn];

void init(){
	scanf("%s",s+1);
}

void solve(){
	int ans,len,n;
	len=strlen(s+1);
	if (s[1]=='-') a[1]=0; else a[1]=1;
	n=1;
	fou(i,2,len){
		if (s[i]!=s[i-1]){
			n++;
			a[n]=a[n-1]^1;
		}
	}
	if (n==1){
		if (a[1]==0) printf("1\n"); else printf("0\n");
		return;
	}
	ans=0;
	if (a[1]==0){
		for(int i=1;i<=n;i+=2){
			a[i]^=1;
			if (i+1<n) a[i+1]^=1;
		}
		ans++;
	}
	fou(i,1,n)
		if (a[i]==0) ans+=2;
	printf("%d\n",ans);
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
//	while (scanf("",)!=EOF){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
