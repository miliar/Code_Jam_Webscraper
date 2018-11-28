#include<stdio.h>
#include<string.h>

int n;
int dab;
char passcode[2000][200];

char* rev(char*str){
	int i;
	char temp, srev[200]={0};
	int end=strlen(str);

	for(i=0;i<end;i++)
	{
		srev[i]=str[end-i-1];
	}

	return srev;
}

int main(){
	int i,j;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%s", passcode[i]);
	}
	for(i=0;i<n;i++){
		for(j=i/*+1*/;j<n;j++){
			//printf("%s\n",rev(passcode[i]));
			if(!strcmp(rev(passcode[i]),passcode[j]))
				{dab=strlen(passcode[i]);  printf("%d %c", dab,passcode[i][dab/2]); return 0; }
			//printf("%s, %s\n",passcode[i],passcode[j]);
		}
	}

	//while(1);
}