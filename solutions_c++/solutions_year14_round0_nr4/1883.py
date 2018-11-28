#include <cstdio>
#include <algorithm>
using namespace std;

int t,i,j,l,n,scr2,scr1;
long double t1[1007],t2[1007];

int main(){
	scanf("%d", &t);
	for(l=0;l<t;l++){
		scanf("%d", &n);
		for(i=0;i<n;i++) scanf("%Lf", &t1[i]);
		for(i=0;i<n;i++) scanf("%Lf", &t2[i]);
		sort(t1,t1+n); sort(t2,t2+n);
/*		for(i=0;i<n;i++) printf("%Lf ", t1[i]);
		puts("");
		for(i=0;i<n;i++) printf("%Lf ", t2[i]);
		puts("");
*/		
		j=scr2=0;
		for(i=0;i<n;i++){
			while(t2[j]<=t1[i] && j<n){
				scr2++; 
				j++;
			}
			j++;
			if(j>=n) break;
		}
		j=n-1; scr1=0;
		for(i=n-1;i>=0;i--){
			while(t2[j]>=t1[i] && j>=0) j--;
			if(j>=0) scr1++;
			j--;
			if(j<0) break;
		}	
		printf("Case #%d: %d %d\n", l+1, scr1, scr2);
	}
	return 0;
}
