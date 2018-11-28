#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <inttypes.h>

int64_t sol_div[9];

bool IsPrime(int64_t n, int base){//Devuelve true si n es primo, false si no.
	
	int64_t i,max;
	
	if (n < 2){	
		sol_div[base]= 1; 	
		return false;
	}
	if (n < 4){
		return true;
	}
	if (n % 2 == 0){
		sol_div[base]= 2;
		return false;
	}
	
	max=(int64_t)sqrt(n)+1;
	
	for(i=3;i<=max;i=i+2){
		if (n%i==0){
			sol_div[base]= i;
			//printf("Divisible por: %" PRId64 "\n",i);
			return false;
		}
	}
	return true;
}

int64_t convertir_base(int *num,int l, int base){//Devuelve el numero en num en base b;
	
	int64_t res=0;
	int i;
	
	for(i=0;i<l;i++){
		res=res+num[i]*pow(base,(l-1)-i);
	}
	
	return res;
}

void printres(int *number,int n){//Imprime el numero en *number
	
	int i;
	
	for(i=0; i<n; i++){
		printf("%d",number[i]);
	}
	printf(" ");
}

bool comprobar(int *number,int n){//Retorna true si es valido como respuesta

	int i;
	int64_t num;
	bool isp;
	
	for(i=2;i<=10;i++){
		num=convertir_base(number,n,i);
		isp=IsPrime(num,i-2);
		if(isp){
			return false;	
		}
	}
	
	return true;
}

void sumabin(int *number,int n){//Suma 1 en num en binario;

	int cnt=n-1;
	
	while(number[cnt]==1){
		number[cnt]= 0;
		cnt--;
	}
	
	number[cnt] = 1;

}

void generador(int *number,int n, int j,int z){//Genera Coin Jam de longitud n;
	
	int *inter_num,i,k,cnt;
	
	number[0]=1;
	number[n-1]=1;
	inter_num=(int*)calloc(n-2,sizeof(int));
	cnt=pow(2,n-2);
	
	printf("Case #%d:\n",z);
	
	for(k=0;k<j;k++){
		if(cnt<=0){
			break;
		}
		
		while(!comprobar(number,n)){
			if(cnt <= 0) {
				break;
			}
			
			sumabin(inter_num,n-2);
			for(i=1;i<=n-2;i++){
				number[i] = inter_num[i-1];
			}
			
			cnt--;
		}
		
		printres(number,n);
		for(i=0;i<9;i++){
			printf("%" PRId64 " ",sol_div[i]);
		}
		
		printf("\n");
		
		sumabin(inter_num,n-2);
		for(i=1;i<=n-2;i++){
			number[i] = inter_num[i-1];
			cnt--;
		}
			
	}
	
}

int main(){
	
	int *number,n,j,z;
		
	scanf("%d",&z);
	scanf("%d",&n);
	scanf("%d",&j);
	

	number=(int*)calloc(n,sizeof(int));
	
	generador(number,n,j,z);
	
	return 0;
}
