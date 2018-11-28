#include <stdio.h>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
double naomi[1010], ken[1010]; int n;
int main(){
	int t;
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &t);
	for(int ind=1; ind<=t; ind++){
		printf("Case #%d: ", ind);
		scanf("%d", &n);
		for(int i=0; i<n; i++) scanf("%lf", &naomi[i]);
		for(int i=0; i<n; i++) scanf("%lf", &ken[i]);
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		int war=0, deceit=0;
		int nli=0, nls = n-1, kli=0, kls = n-1;
		for(int i=n-1; i>=0; i--){
			if(naomi[i]>ken[kls]){
				kli++;
				war++;
			}else if(naomi[i]<ken[kls]){
				kls--;
			}
		}
		nli=0; nls = n-1; kli=0; kls = n-1;
		for(int i=0; i<n; i++){
			if(naomi[i]<ken[kli]){
				kls--;
			}else if(naomi[i]>ken[kli]){
				kli++;
				deceit++;
			}
		}
		printf("%d %d\n", deceit, war);
	}
	return 0;
}