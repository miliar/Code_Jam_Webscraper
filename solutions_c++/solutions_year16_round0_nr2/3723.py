#include <bits/stdc++.h>

int c,t,usaqui,cont=0,aux=0,i=0,tes=1;
char dig,s[200];

int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%s",s);
		while(aux<strlen(s)){
			while(i<strlen(s)){
				if(s[i]=='-'){
					if(i!=(strlen(s)-1))
						for(int j = i ; j < strlen(s) ; j++){
							if(s[j]=='+'){
								usaqui=j-1;
								break;
							}
							if(j==(strlen(s)-1))
								usaqui=j;
						}
					else
						usaqui=i;
					for(int j = 0 ; j <= usaqui ; j++){
						if(s[j]=='+'){
							s[j]='-';
							aux--;
						}
						else{
							s[j]='+';
							aux++;
						}
					}
					cont++;
					i=0;	
				}
				else{
					aux++;
					i++;
				}
			}
		}
		printf("Case #%d: %d\n",tes++,cont);
		cont=0;
		i=0;
		aux=0;
	}
}
