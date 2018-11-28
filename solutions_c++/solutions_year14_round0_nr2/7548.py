#include <stdio.h>





int main(){

	FILE *entree, *sortie;
	double p,a,x,c,f;
	double t,tc;
	int n,i=1;;
	sortie=fopen("B-largeS.in","w");
									
	entree=fopen("B-large.in","r");
											
		fscanf(entree,"%d",&n);
											
		while(n!=0){								
			
		fscanf(entree,"%lf %lf %lf",&c,&f,&x);
		t=0;
		p=2;
		tc=c/p;
		a=x/p;
			while(a>((x/(p+f))+tc)){
				
				t+=tc;
				p+=f;
				tc=c/p;
				a=x/p;
			}
			p+=f;	
			
			
			t=t+a;
			
		fprintf(sortie,"Case #%d: %.7lf\n",i++,t);	
		n-=1;
}
fclose(sortie);
fclose(entree);
	return 0;

}
