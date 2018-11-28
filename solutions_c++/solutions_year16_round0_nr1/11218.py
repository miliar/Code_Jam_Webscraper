#include<iostream>
#include<cstdio>
#include<algorithm>

#define L 15

using namespace std;

bool dig[L];

void update_dig(long long x){
	
	while(x > 0LL){
		
		int d = x % 10;
		dig[d] = true;

		x /= 10;
	}
	
}

bool verif_dig(){

	for(int i = 0; i <= 9; i++)
		if(!dig[i]) return false;
	
	return true;
}


int main(){
	
	int nc;
	scanf("%d", &nc);

	for(int caso = 1; caso <= nc; caso++){
			
		int x;
		scanf("%d", &x);
		
		printf("Case #%d: ", caso);
		
		for(int i = 0; i < L; i++) dig[i] = false;
		
		if(x == 0) printf("INSOMNIA\n");
		else{

			update_dig(x);
			int k = 1;
			while(!verif_dig()){
				k++;
				update_dig(x * k);
				//printf("x %lld\n", x * k);
				
			}		
			printf("%lld\n", x * k);
		}

	}

	return 0;
}
