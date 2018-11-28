#include<cstdio>
#include<algorithm>
using namespace std;

#define EPS 1e-19
#define N 1005
int T, n, ptN, ptK, ans2, ans1;
double Na[N], Ke[N];
int main(){
	
	
	freopen("GCJ14_QR_Dlarge.in","r",stdin);
	freopen("GCJ14_QR_Dlarge.out","w", stdout);

scanf("%d",&T);
	for (int t = 0; t < T; t++){
		ans1 = ans2 = 0;
		scanf("%d",&n);
		for (int i = 0; i < n; i++)scanf("%lf",&Na[i]); 
		for (int i = 0; i < n; i++)scanf("%lf",&Ke[i]); 		
		sort(Na, Na+n); sort(Ke, Ke+n);
		for (int i = 0; i < n; i++){
			int tmp = 0;
			for (int j = 0; j < n-i; j++){
				if (Na[i+j] > Ke[j]+EPS)tmp++;
			}
			ans1 = max(ans1, tmp);
		} 
		
		ptN = ptK = ans2 = 0;
		while (ptK < n){
			if (Ke[ptK] > Na[ptN]+EPS){ ptK++; ptN++;}
			else{ ptK++; ans2++;}
		}
		
		printf("Case #%d: %d %d\n", t+1, ans1, ans2);
	}
	return 0;
}
