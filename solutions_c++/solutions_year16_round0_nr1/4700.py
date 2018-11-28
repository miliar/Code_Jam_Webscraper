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

const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int n;
bool f[20];

void init(){
	scanf("%d",&n);
}

void cal(LL x)
{
	while (x){
		f[x%10]=true;
		x/=10;
	}
}

void solve(){
	if (n==0){
		printf("INSOMNIA\n");
		return;
	}
	LL now;
	bool flag;
	memset(f,false,sizeof(f));
	fou(i,1,100000000){
		now=(LL)n*i;
		cal(now);
		flag=true;
		fou(j,0,9)
			if (!f[j]){
				flag=false;
				break;
			}
		if (flag){
			printf("%lld\n",now);
			return;
		}
	}
	printf("INSOMNIA\n");
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
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
