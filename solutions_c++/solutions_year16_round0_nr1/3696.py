#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
LL n,k;
bool vis[10];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("o1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int i=0;i<T;i++){
		scanf("%I64d",&n);
		printf("Case #%d: ",i+1);
		if (!n) {
			printf("INSOMNIA\n");
		    continue;
		}
		else{
			int sum=0;
			k=1;
			memset(vis,false,sizeof(vis));
			while (sum!=10){
				LL l=k*n;
				while (l){
					if (!vis[l%10]){
						vis[l%10]=true;
						sum++;
					}
					l/=10;
				}
				k++;
			}
			printf("%I64d\n",(k-1)*n);
		}
    }
    return 0;
}
