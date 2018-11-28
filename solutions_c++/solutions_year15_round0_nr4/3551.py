#include<stdio.h>
int main(void){
	int x,r,c;
	int t,ccc;
	FILE *f,*f2;

	f=fopen("D-small-attempt1.in","r+");
	f2=fopen("output_d.txt","w+");

	fscanf(f,"%d",&t);
	ccc=0;
	while(t--){
		ccc++;
		fscanf(f,"%d %d %d",&x,&r,&c);
		fprintf(f2,"Case #%d: ",ccc);
		if((r*c)%x != 0) {
			fprintf(f2,"RICHARD\n");
		}
		else{
			if(x==1){
				fprintf(f2,"GABRIEL\n");
			}
			else if(x>=3 && (c==1 || r==1)){
				fprintf(f2,"RICHARD\n");
			}
			else if(x==4 && (c==2 || r==2)){
				fprintf(f2,"RICHARD\n");
			}
			else if(r*c==8 && x==4){
				fprintf(f2,"RICHARD\n");
			}
			else{
				fprintf(f2,"GABRIEL\n");
			}
		}

	}
	return 0;
}