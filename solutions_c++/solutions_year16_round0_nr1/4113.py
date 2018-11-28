#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
const int MAX_N=1000010;

inline int solve(int n)
{
	int vis[15];
	memset(vis,0,sizeof(vis));
	for(int i=1;i<=100;i++){
		int tmp=n*i;
		while(tmp){
			vis[tmp%10]=1;
			tmp/=10;
		}
		int ok=1;
		for(int j=0;j<=9;j++){
			if(vis[j]==0){
				ok=0;
				break;
			}
		}
		if(ok) return n*i;
	}
	return -1;
}

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("Aout.txt","w",stdout);
	int T,n,cases=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		printf("Case #%d: ",++cases);
		if(n==0) printf("INSOMNIA\n");
		else printf("%d\n",solve(n));
	}
	return 0;
}
