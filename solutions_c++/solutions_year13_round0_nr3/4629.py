#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


int espalindromo(unsigned long long n){
	char num[200];
	
	sprintf(num,"%llu",n);
	
	int i=0,j=strlen(num)-1;
	
	for(;j>i;i++,j--){
		if(num[i]!=num[j]){
			return 0;
		}
	}
	
	
	return 1;
}

unsigned long long explorar(unsigned long long li,unsigned long long ls){
	unsigned sqli=sqrt((long double) li);
	
	unsigned  long long n=sqli;
	
	unsigned long long cant=0;
	unsigned long long num=0;
	
	
	for(;1;n++){
		if(espalindromo(n)){
			num=n*n;
			if(num>ls){break;}
			if(num>=li && espalindromo (n*n)){
				cant++;
				//printf("%llu %llu\n",n,num);
			}
			
		}
	}
	
	return cant;
	
}



int main(int argc,char**argv){
	
	freopen("FaS.txt","r",stdin);
	
	if(argc>1){
		freopen(argv[1],"r",stdin);
		
		
		char auxchar[200]={0};
		strcat(auxchar,argv[1]);
		strcat(auxchar,".out.txt");
		
		freopen(auxchar,"w",stdout);
	}
	
	
	
	int cant;
	scanf("%d",&cant);
	
	for(int no=0;no<cant;no++){
		
		unsigned long long ls,li,res;
		
		scanf("%llu %llu",&li,&ls);
		
		
		
		res=explorar(li,ls);
		
		printf("Case #%d: %llu\n",no+1,res);
		
		
		
		
		
		
		
		
		
		
		
		
		
	}
	return 0;
}
