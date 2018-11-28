#include <stdio.h> 
#include <string.h> 
#include <math.h> 
int main(){
	FILE *fp;
	char fileName[] = "C-small-attempt0.in",outputfileName[]="B-large.out";
	int i,k,j,t,sta[10000];
	unsigned int m, n;
	unsigned int a[13] = {1,4,9,121,484,101*101,111*111,121*121,202*202,212*212,1001*1001,1111*1111,2002*2002};

	if((fp=fopen(fileName, "r")) == NULL){
		printf("Can't read file");
		return -1;
   }

	fscanf(fp, "%d ",&t);
for(k=1;k<=t;++k){
	j=0;
	fscanf(fp, " %d %d", &m, &n);
	
	for(i=0;i<13;++i){
		if(m<=a[i] && n>=a[i]){
			++j;
		}
	}

	sta[k] = j;
}


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
