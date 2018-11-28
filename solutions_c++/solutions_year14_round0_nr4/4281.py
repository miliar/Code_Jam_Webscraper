#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

#define fr(a,b,c) for(int a=b;a<c;a++)
#define rp(a,b) fr(a,0,b)
#define cl(a,b) memset(a,b,sizeof(a))

int a[1010],b[1010];
bool used[1010];

const int gap=100000;

int n;

int main(){
	int t; scanf("%d",&t); t++;
	fr(cas,1,t){
		scanf("%d",&n);
		double aux;
		rp(i,n){
			scanf("%lf",&aux);
			a[i] = round(aux*gap);
		}
		sort(a,a+n);
		rp(i,n){
			scanf("%lf",&aux);
			b[i] = round(aux*gap);
		}
		sort(b,b+n);
		int cont=0,cont2=0;
		cl(used,0);
		for(int i=n-1;i>=0;i--){
			for(int j=0;j<n;j++){
				if(!used[j] && b[j] > a[i]){
					used[j] = 1;
					goto pulo;
				}
			}
			cont2++;
			for(int j=0;j<n;j++) if(!used[j]){
				used[j]=1;
				break;
			}
			pulo:;
		}
		int j=0;
		rp(i,n){
			if(a[i] > b[j]){
				j++;
				cont++;
			}
		}
		// rp(i,n) printf("%5d ",a[i]); printf("\n"); rp(i,n) printf("%5d ",b[i]); printf("\n");
		printf("Case #%d: %d %d\n",cas,cont,cont2);
	}
	return 0;
}
