#include <cstdio>

int main()
{
	int T;
	FILE* r = fopen("D-small-attempt0.in","r");
	FILE* w = fopen("D.out","w");
	fscanf(r,"%d",&T);
	for(int i=0;i<T;i++){
		int K,C,S;
		fscanf(r,"%d%d%d",&K,&C,&S);
		fprintf(w,"Case #%d:",i+1);
		for(int j=0;j<S;j++){
			fprintf(w," %d",(j+1));
		}
		fprintf(w,"\n");
	}
	fclose(r);
	fclose(w);
	return 0;
}
