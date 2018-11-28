#include <stdio.h> 
#include <math.h> 
int main(){
	FILE *fp;
	char fileName[] = "A-small-attempt0.in",outputfileName[]="B-large.out";
	int k,t,sta[6000];
	unsigned int m, n,temp;

	if((fp=fopen(fileName, "r")) == NULL){
		printf("Can't read file");
		return -1;
   }

	fscanf(fp, "%d ",&t);
for(k=1;k<=t;++k){
	fscanf(fp, " %d %d", &m, &n);
	temp = m+m-1;
	sta[k] =  ((int)sqrt(temp*temp+8*n) - temp)/4;
}
fclose(fp);

	if((fp=fopen(outputfileName, "w")) == NULL){
		printf("Can't write file");
		return -1;
    }

for(k=1;k<=t;++k){
	fprintf(fp,"Case #%d: %d\n",k, sta[k]);
}
	fclose(fp);
	return 1;
}