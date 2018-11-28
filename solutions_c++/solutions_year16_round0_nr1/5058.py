#include <bits/stdc++.h>

using namespace std;

bool sync_with_stdio (bool sync = false);

typedef long long ll;
int vet[11];

int main(){

	int t, cont = 1, ans, i;
	int n;
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		if(n == 0)
			printf("Case #%d: INSOMNIA\n", cont++);
		else{
			memset(vet, 0, sizeof(vet));
			ans = 0;
			ll aux = 0;
			for(i = 1; ans < 10; i++){
				aux = n*i;
				while(aux){
					if(vet[aux%10] == 0){
						vet[aux%10] = 1;
						ans++;
					}
					aux = aux/10; 
				}
				
				
			}
			printf("Case #%d: %lld\n", cont++, (i-1)*(ll)n);
			
		}
		
	}

	return 0;
}
