#include<iostream>

#define lim 800

FILE *inp, *out;

char str[1001],resStr[5000];

int main(){
	int i,j,T,counter,L,R;
	inp = fopen("inp.in","r");
	out = fopen("out.txt","w");
	fscanf(inp,"%d",&T);
	for(i=1;i<=T;++i)
	{
		fscanf(inp,"%s",str);
		fprintf(out,"Case #%d: ",i);
		printf("Case #%d: ",i);		
		L=R=2500;
		resStr[L]=str[0];
		for(j=1;str[j]!='\0';++j)
		{
			if((int)str[j]>=(int)resStr[L])
			{
				resStr[--L]=str[j];
			}
			else
			{
				resStr[++R]=str[j];
			}
		}
		for(j=L;j<=R;++j)
		{	
			fprintf(out,"%c",resStr[j]);				
			printf("%c",resStr[j]);
		}		
		fprintf(out,"\n");			
		printf("\n");
	}
	return 0;
}
