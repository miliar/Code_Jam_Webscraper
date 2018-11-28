#include<stdio.h>
int i,j,t,k,n,x[10000][3],y[400],ti[400],ki[400],p,ck[400][400];
int q,a,b,z[400][400],ctr,s,u,v,ch[400],w;
int main(){
FILE * fin, *fout;
fin =fopen("c:\\input.txt","r");
fout=fopen("c:\\output","w");
fscanf(fin,"%d",&t);
printf("%d",t);
x[0][2]=0;
x[1][2]=x[4][2]=x[9][2]=x[121][2]=x[484][2]=1;
for(p=1;p<=1024;p++){
	x[p][0]=0;//palin
	x[p][1]=0;//perf sq
	if(x[p][2])
		x[p][2]+=x[p-1][2];
	else
		x[p][2]=x[p-1][2];		
	if(p>=1&&p<=9){
		x[p][0]=1;
	}
	if(p<=31){
		x[p*p][1]=1;
	}
	
}


for (i=1;i<=t;i++){

	
		
	fscanf(fin,"%d%d",&a,&b);
	
	
	fprintf(fout,"Case #%d: %d",i,x[b][2]-x[a-1][2]);
	
	fprintf(fout,"\n");
}
fclose(fin);
fclose(fout);
return 0;
}
