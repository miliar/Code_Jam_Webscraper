#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#define MAX 20
using namespace std;
int V[MAX];

int main(){
	int t,a,b,aux; int caso = 1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&a); a--;
		memset(V,0,sizeof V);
		for(int i = 0;i < 4;i++){
			for(int j = 0;j < 4;j++){
				scanf("%d",&aux);
				if(i == a) V[aux]++;
			}
		}
		
		scanf("%d",&b); b--;
		for(int i = 0;i < 4;i++){
			for(int j = 0;j < 4;j++){
				scanf("%d",&aux);
				if(i == b) V[aux]++;
			}
		}
		int cont = 0; int res = 0;
		for(int  i = 0;i < MAX;i++) if(V[i] == 2) cont++,res = i;
		printf("Case #%d: ",caso++);
		if(cont == 1) printf("%d\n",res);
		else if(cont > 1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	return 0;
}
