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
#include<cmath>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

LL ans[100];
int n,m,b[100];

void init(){
	n=16;
	m=50;
}

void change(LL now)
{
	int tot=0;
	while (now){
		b[++tot]=now & 1;
		now>>=1;
	}
}

bool isprime(LL &x)
{
	int ed=(int)(sqrt((double)x)+1e-7);
	fou(i,2,ed)
		if (x%i==0){
			x=i;
			return false;
		}
	return true;
}

bool check(LL now)
{
	LL k;
	change(now);
	fou(i,2,10){
		k=1;ans[i]=0;
		fou(j,1,n){
			if (b[j]) ans[i]+=k;
			k*=i;
		}
	}
	fou(i,2,10)
		if (isprime(ans[i])) return false;
	
	fod(i,n,1) printf("%d",b[i]);
	printf(" ");
	fou(i,2,9) printf("%lld ",ans[i]);
	printf("%lld\n",ans[10]);
	return true;
}

void solve(){
	LL st,ed;
	st=(1ll<<(n-1))+1;
	ed=(1ll<<n)-1;
	for (LL i=st;i<=ed;i+=2){
		if (check(i)) m--;
		if (m==0) return;
	}
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	int T=1;
	fou(i,1,T){
//	while (scanf("",)!=EOF){
		printf("Case #%d:\n",i);
		init();
		solve();
	}
	return 0;
}
