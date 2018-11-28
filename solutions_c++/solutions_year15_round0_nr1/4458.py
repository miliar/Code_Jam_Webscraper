#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void main(){
	int T,Smax,k;
	FILE *fp;
	int i,j,pre,invitek,invite;
	char *s;

	s=(char *)malloc(sizeof(char)*1002);
	fp=fopen("A-small-attempt1.in","r");
	fscanf(fp,"%d\n",&T);
	for(i=0;i<T;i++){
		s=fgets(s,1500,fp);
		Smax=atoi(strtok(s," "));
		s=strtok(NULL," ");
		pre=0;
		invite=0;
		for(j=0;j<=Smax;j++){
			if((j-pre)>0)
				invitek=j-pre;
			else
				invitek=0;
			pre=pre+(s[j]-48)+invitek;
			invite=invite+invitek;
		}
		printf("Case #%d: %d\n",i+1,invite);
	}

	fclose(fp);
}