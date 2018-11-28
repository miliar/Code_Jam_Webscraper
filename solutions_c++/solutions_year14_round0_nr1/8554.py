#include<cstdio>
#include<map>
using namespace std;
map<int,int> mark;
int mat[60][60];
int main( )
{ 
FILE *g=fopen("girdi.txt","r");
FILE *f=fopen("sonuc.txt","w");
int t,syc=0,tut,t1;
fscanf(g," %d",&t1);
for(int i=1;i<=t1;i++){
	syc=0;
	fscanf(g,"%d",&t);
 for(int j=1;j<=4;j++)	
	for(int k=1;k<=4;k++) fscanf(g," %d",&mat[j][k]);
for(int j=1;j<=4;j++) mark[mat[t][j]]=i;


	fscanf(g,"%d",&t);
 for(int j=1;j<=4;j++)	
	for(int k=1;k<=4;k++) fscanf(g," %d",&mat[j][k]);
for(int j=1;j<=4;j++) if(mark[mat[t][j]]==i) tut=mat[t][j],syc++;
fprintf(f,"Case #%d: ",i);
if(syc==1) fprintf(f,"%d\n",tut);
if(syc>1) fprintf(f,"Bad magician!\n");
if(syc==0)fprintf(f,"Volunteer cheated!\n");
}
}
