#include <stdio.h>

int main(){
	FILE *fin = fopen("input.txt","r"), *fout;
	if(!fin){printf("no input\n"); return 0;}
	fout = fopen("output.txt","w");
	int i, j, T=0;
	if(fscanf(fin,"%d",&T)!=1)return 0;
	for(i=1; i<=T; i++){
		int s1, s2;
		int m1=0, m2=0;
		int t;
		fscanf(fin, "%d", &s1);
		for(j=1; j<s1;j++)
			fscanf(fin,"%d%d%d%d",&t,&t,&t,&t);
		for(j=0; j<4;j++){
			fscanf(fin,"%d",&t);
			m1 |= (1<<t);
		}
		for(j=s1+1; j<=4;j++)
			fscanf(fin,"%d%d%d%d",&t,&t,&t,&t);
		fscanf(fin, "%d", &s2);
		for(j=1; j<s2;j++)
			fscanf(fin,"%d%d%d%d",&t,&t,&t,&t);
		for(j=0; j<4;j++){
			fscanf(fin,"%d",&t);
			m2 |= (1<<t);
		}
		for(j=s2+1; j<=4;j++)
			fscanf(fin,"%d%d%d%d",&t,&t,&t,&t);
		m1&=m2;
		if(!m1)fprintf(fout, "case #%d: %s\n", i, "Volunteer cheated!");
		else{
			for(j=0; !(m1&1); j++)
				m1>>=1;
			if(m1>>1)fprintf(fout, "case #%d: %s\n", i, "Bad magician!");
			else fprintf(fout, "case #%d: %d\n", i, j);
		}
	}
	fclose(fin); fclose(fout);
	return 0;
}