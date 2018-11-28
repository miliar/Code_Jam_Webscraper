    #include <bits/stdc++.h>
     
    using namespace std;
     
    int vet[10];
    int aux;
     
    int check(int x){
    	while(x > 0){
    		int r = x % 10;
    		x = x / 10;
    		if(vet[r] == 0)
    			aux++;
    		vet[r] = 1;
    	}	
    }
     
    int main(){
    	int n, x, out;
     
    	scanf("%d", &n);
     
    	for(int cases = 1; cases <= n; cases++){
    		aux = 0;
    		memset(vet, 0, sizeof(vet));
    		scanf("%d", &x);
     
		if(x != 0)
    			for(int i = x; i <= 120 * x; i += x){
    				check(i);
     
    				if(aux >= 10){
    					out = i;
    					break;
    				}
    			}
     
    		if(aux >= 10){
    			printf("Case #%d: %d\n", cases, out);
    		} else {
    			printf("Case #%d: INSOMNIA\n", cases);
    		}
    	}	
     
    	return 0;
    }
