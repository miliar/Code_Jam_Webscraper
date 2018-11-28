#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int t,n,i,j,tmp,ans,tes;
int a[1000007];
int mem[1007][1007];

int DP(int dari, int ke) {
	if (dari <= ke) return 0;
	if (mem[dari][ke] != -1) return mem[dari][ke];
	
	return mem[dari][ke] = min(1 + DP(dari/2,ke) + DP(dari - dari/2,ke),1 + DP(dari-ke,ke));
}

int main() {
	for (i=1 ; i<=1000 ; i++)
		for (j=1 ; j<=1000 ; j++)
			mem[i][j] = -1;

	for (i=1 ; i<=1000 ; i++)
		for (j=1 ; j<=1000 ; j++)
			DP(i,j);
			
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d",&n);
		for (i=1 ; i<=n ; i++) scanf("%d",&a[i]);
		
		ans = 999999999;
		for (i=1 ; i<=1000 ; i++) {
			tmp = i;
			for (j=1 ; j<=n ; j++) tmp += DP(a[j],i);
			ans = min(ans,tmp);
		}
		
		printf("Case #%d: %d\n",tes,ans);
	}
}
