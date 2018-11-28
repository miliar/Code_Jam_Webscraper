#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main()
{
	//FILE *fi=fopen("sample.in","r"), *fo=fopen("sample.out","w");
	FILE *fi=fopen("A-small-attempt0.in","r"), *fo=fopen("A-small-attempt0.out","w");
	//FILE *fi=fopen(".in","r"), *fo=fopen(".out","w");
	if(!fi||!fo){printf("Error opening files!\n");getchar();return -1;}
	int T=0,i=0,j=0,f=0,s=0,k=0;
	fscanf(fi,"%d",&T);printf("%d\n",T);
	int a1[4][4],a2[4][4];
	for(int i=0;i<T;++i)
	{
            fscanf(fi,"%d",&f);--f;printf("%d\n",f);
            for(j=0;j<4;++j){fscanf(fi,"%d %d %d %d",&a1[j][0],&a1[j][1],&a1[j][2],&a1[j][3]);printf("%d %d %d %d\n",a1[j][0],a1[j][1],a1[j][2],a1[j][3]);}
            fscanf(fi,"%d",&s);--s;printf("%d\n",s);
            for(j=0;j<4;++j){fscanf(fi,"%d %d %d %d",&a2[j][0],&a2[j][1],&a2[j][2],&a2[j][3]);printf("%d %d %d %d\n",a2[j][0],a2[j][1],a2[j][2],a2[j][3]);}
            int cnt=0, val=0;
            for(j=0;j<4;++j)
            {
                            for(int k=0;k<4;++k){
                            if(a1[f][j]==a2[s][k]){cnt++;val=a1[f][j];}}
            }
            if(!cnt){fprintf(fo,"Case #%d: Volunteer cheated!\n",i+1);}
            else if(1==cnt){fprintf(fo,"Case #%d: %d\n",i+1,val);}
            else{fprintf(fo,"Case #%d: Bad magician!\n",i+1);}
    }
	fflush(fo);fclose(fi);fclose(fo);
	getchar();return 0;
}
