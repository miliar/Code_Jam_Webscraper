#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int t;
	scanf("%d", &t);
	int cont=1;
	while(cont<=t){
		int naomiDecWar=0;
		int quantidade;
		
		scanf("%d", &quantidade);
		vector <float> ken, naomi;
		float aux;
		for(int i=0; i<quantidade; i++){
			scanf("%f", &aux);
			naomi.push_back(aux);
		}
		for(int i=0; i<quantidade; i++){
			scanf("%f", &aux);
			ken.push_back(aux);
		}
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		int i=0;
		int iniK=0, fimK=quantidade-1, iniN=0, fimN=quantidade-1;
		while(iniN<=fimN){
				if(naomi[iniN]<ken[iniK]){
					fimK--;
					iniN++;	
				}else{
					iniK++;
					iniN++;
					naomiDecWar++;
				}
		}
		int q,n=quantidade-1, naomiWar=0, k=quantidade-1;
		if(quantidade==1){
			if(naomi[0]>ken[0]){ 
				naomiWar=1;
			}
		}else{
			while(!naomi.empty()){
				if(naomi[n] > ken[k]){ 
					naomiWar++;
					naomi.pop_back();
					ken.erase(ken.begin());
				}else{
					q=k;
					while(naomi[n]<ken[q]) q--;
					for(int x=q+1; x<k; x++) ken[x]=ken[x+1];
					naomi.pop_back();
					ken.pop_back();
				}
					n--;
					k--;
				}

			}
		printf("Case #%d: %d %d\n", cont, naomiDecWar, naomiWar);
		cont++;
	}
	return 0;
}