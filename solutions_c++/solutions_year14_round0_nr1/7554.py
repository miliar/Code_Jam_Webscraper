#include <stdio.h>

int comp(int *a, int *b,int *c){
	
	int o,i,j,k;
	k=0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(a[i]==b[j]) {
				k++;
				
				*c=i;
			}
		}
	}
	return k;
}



int main(){
	int comp(int *, int *,int *);
	int A[4][4],B[4][4];
	FILE *entree, *sortie;
	int i,j,n,k,l,o,m=1;
	int *x,*y;
	char ligne[9],g;
	sortie=fopen("output.in","w");
									
	entree=fopen("input.in","r");
											
		fscanf(entree,"%d",&n);
											
		while(n!=0){								
			
			fscanf(entree,"%d",&j);	
			for(i=0;i<4;i++) {
			
				fscanf(entree,"%d %d %d %d",&A[i][0],&A[i][1],&A[i][2],&A[i][3]);
			}
																	
			
			fscanf(entree,"%d",&k);			
			for(i=0;i<4;i++) {
				
			fscanf(entree,"%d %d %d %d",&B[i][0],&B[i][1],&B[i][2],&B[i][3]);	
		}
		
		
		i=comp(&A[j-1][0],&B[k-1][0],&l);

		if(i==1){
			
				fprintf(sortie,"case #%d: %d\n",o++,A[j-1][l]);
		}else{
			if(i==0){
				fprintf(sortie,"case #%d: Volunteer cheated!\n",o++);
				
			}else{
					fprintf(sortie,"case #%d: Bad magician!\n",o++);
			}
		}
		n-=1;
	
}
fclose(sortie);
fclose(entree);
	return 0;

}
