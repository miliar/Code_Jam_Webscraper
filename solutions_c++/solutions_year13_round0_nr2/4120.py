#include<stdio.h>
int x,i,j,n,m,t,a[100][100],b[100][100],maxi[100],maxj[100],no;
int main(){
FILE * fin, *fout;
fin =fopen("c:\\input.txt","r");
fout=fopen("c:\\output","w");
fscanf(fin,"%d",&t);


for (x=1;x<=t;x++){

	
		
	fscanf(fin,"%d%d",&n,&m);
	for(i=0;i<n;i++){
		maxi[i]=0;
		for(j=0;j<m;j++){
			fscanf(fin,"%d",&a[i][j]);
			maxi[i]=a[i][j]>maxi[i]?a[i][j]:maxi[i];
			b[i][j]=2;
		}
	}
	for(j=0;j<m;j++){
		maxj[j]=0;
		for(i=0;i<n;i++){
			maxj[j]=a[i][j]>maxj[j]?a[i][j]:maxj[j];
		}
	}
	no=0;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			b[i][j]=maxi[i]<maxj[j]?maxi[i]:maxj[j];
			if (b[i][j]!=a[i][j]){
				no=1;
				break;
			}
		}
		if(no==1)
			break;
	}
	
	fprintf(fout,"Case #%d: %s",x,no?"NO":"YES");
	
	fprintf(fout,"\n");
}
fclose(fin);
fclose(fout);
return 0;
}
