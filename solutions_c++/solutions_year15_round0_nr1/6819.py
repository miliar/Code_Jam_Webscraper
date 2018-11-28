#include <stdio.h>
#include <string.h>
char Cad[2000];
int Smax,lg,standing,res;
int main(){
	freopen("data.in","r",stdin);  
    	freopen("data.out","w",stdout); 
	int T;
	scanf("%d",&T);
	//printf("--%d\n",T);
	for(int c=1;c<=T;c++){
		scanf("%d %s",&Smax, Cad);
		lg=strlen(Cad);	//Smax+1	
		//printf("%d %s [%d]\n",Smax, Cad,lg);
		standing=0;
		res=0;
		for(int i=0;i<lg;i++){
			//printf("d");
			if( Cad[i]-'0' !=0 ){
				while(i>standing){
					standing++;
					res++;
				}
				standing+=Cad[i]-'0'; 	
			}	
		}
		printf("Case #%d: %d\n",c,res);
	}
	return 0;
}
