#include <cstdio>
using namespace std;

int licz, dod, ile, il, k;

int main(){
	scanf("%d", &ile);
	for(int t=0; t<ile; t++){
		licz=0;
		scanf("%d", &il);
		scanf("%1d", &dod);
		
		for(int i=1; i<=il; i++){
			scanf("%1d", &k);
			if(k>0 & dod<i){
				licz+=i-dod;
				dod+=i-dod;
			}
			dod+=k;
		}
		printf("Case #%d: %d\n", t+1, licz);
	}
}
