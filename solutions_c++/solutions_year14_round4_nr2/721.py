#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>

using namespace std;

int i,j,k,tmp,kanan,kiri,ans,t,n,idx,minim,tes;
int a[1000007];

int main() {
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d",&n);
		for (i=0 ; i<n ; i++) scanf("%d",&a[i]);
		
		kiri = 0;
		kanan = n-1;
		ans = 0;
		
		for (i=0 ; i<n ; i++) {
			minim = 2000000000;
			idx = 0;
			for (j=kiri ; j<=kanan ; j++)
				if (a[j] < minim) {
					minim = a[j];
					idx = j;
				}
		
			if (abs(kiri-idx) <= abs (kanan-idx)) {
				ans += abs(kiri-idx);
				
				k = idx;
				while (k != kiri) {
					tmp = a[k];
					a[k] = a[k-1];
					a[k-1] = tmp;
					
					k--;
				}
				
				kiri++;
			} else {
				ans += abs(kanan-idx);
			
				k = idx;
				while (k != kanan) {
					tmp = a[k];
					a[k] = a[k+1];
					a[k+1] = tmp;
					
					k++;
				}
			
				kanan--;
			}
		}
		
		printf("Case #%d: %d\n",tes,ans);
	}
}