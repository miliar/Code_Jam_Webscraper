#include <bits/stdc++.h>
using namespace std;
#define MAX 1853020188851841
int main(){
	bool naoe=false,nmais1=true,nmais2=false,nmais3=false,nmais4=false,nmais5=false,nmais6=false,nmais7=false,nmais8=false,nmais9=false,nmais10=false,nfizval=true;
	string b = "1000000000000001";
	int t,n,k,vet[20];
	scanf("%d",&t);
	scanf("%d %d",&k,&n);
	unsigned long long int at,val =1000000000000001,aux,pot = 10;
	aux=val;
	int cont,pos=15;
	printf("Case #1:\n");
	while(n){
		b = to_string(aux);
		cont = 0;
		if(aux==1000000000000001 and nfizval==true){
			for(unsigned long long int p = 2 ; p <=10 ; p++){
					at = stoll(b,NULL,p);
					for(unsigned long long int m=2; m<sqrt(at); m++){
	       				if(at%m==0){
	       					vet[p]=m;
							naoe=true;
							cont++;
							break;					
	       				}
	       				if(m==(sqrt(at)-1))
	       					naoe=false;
	    			}
	    			if(naoe==false){
	    				break;
	    				cont=0;
					}
					naoe=false;
					if(cont==9){
						cout << b << " ";
						for(int p = 2 ; p<=10 ; p++)
							if(p!=10)
								printf("%d ",vet[p]);
							else
								printf("%d\n",vet[p]);
						n--;
					}
					
			}
			if(aux==1000000000000001)
				nfizval=false;
		}
		else{
			if(aux!=1000000000000001){
				for(unsigned long long int p = 2 ; p <=10 ; p++){
					at = stoll(b,NULL,p);
					for(unsigned long long int m=2; m<sqrt(at); m++){
	       				if(at%m==0){
	       					vet[p]=m;
							naoe=true;
							cont++;
							break;					
	       				}
	       				if(m==(sqrt(at)-1))
	       					naoe=false;
	    			}
	    			if(naoe==false){
	    				break;
	    				cont=0;
					}
					naoe=false;
					if(cont==9){
						printf("%s ",b.c_str());
						for(int p = 2 ; p<=10 ; p++)
							if(p!=10)
								printf("%d ",vet[p]);
							else
								printf("%d\n",vet[p]);
						n--;
					}
					
			}
				
			}
		}
		aux+=pot;
		pot*=10;
		if(aux==1111111111111111){
			aux=val;
			pot=100;
		}
		if(aux==1111111111111101){
			aux=val;
			pot=1000;
		}
		if(aux==1111111111111001){
			aux=val;
			pot=10000;
		}
		if(aux==1111111111110001){
			aux=val;
			pot=100000;
		}
		if(aux==1111111111100001){
			aux=val;
			pot=1000000;
		}
		if(aux==1111111111000001){
			aux=val;
			pot=10000000;
		}
		if(aux==1111111110000001){
			aux=val;
			pot=100000000;
		}
		if(aux==1111111100000001){
			aux=val;
			pot=1000000000;
		}
		if(aux==1111111000000001){
			aux=val;
			pot=10000000000;
		}
		if(aux==1111111000000001){
			aux=val;
			pot=10000000000;
		}
		if(aux==1111110000000001){
			aux=val;
			pot=100000000000;
		}
		if(aux==1111100000000001){
			aux=val;
			pot=1000000000000;
		}
		if(aux==1111000000000001){
			aux=val;
			pot=10000000000000;
		}
		if(aux==1110000000000001){
			aux=val;
			pot=100000000000000;
		}
	}
	
}             
