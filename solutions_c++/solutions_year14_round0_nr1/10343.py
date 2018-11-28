#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    FILE *f1,*f2;
f1=fopen("small.in","r");
f2=fopen("output.txt","w");
int t;
fscanf(f1,"%d",&t);
int grid1[4][4],grid2[4][4];
int ans1,ans2;
int* ans=(int *)malloc(t*sizeof(int));
int* found=(int *)malloc(t*sizeof(int));
int i,j,k;

if(t>100&&t<1)
{
     fclose(f1);
     fclose(f2);
     return 0;
}

for(i=0;i<t;i++)
{
	ans[i]=found[i]=0;
	fscanf(f1,"%d",&ans1);
	if(ans1>4&&ans1<1)
	{
	      fclose(f1);
	      fclose(f2);
	      return 0;
	}
	for(j=0;j<4;j++)
		for(k=0;k<4;k++)
		{
		fscanf(f1,"%d",&grid1[j][k]);
	//	printf("\n%d",grid1[j][k]);
        if(grid1[j][k]>16&&grid1[j][k]<1)
		{
			fclose(f1);
			fclose(f2);
			return 0;
		}
	  }
	fscanf(f1,"%d",&ans2);
	if(ans2>4&&ans2<1)
	{
	fclose(f1);
	   fclose(f2);
	   return 0;
     }
	for(j=0;j<4;j++)
		for(k=0;k<4;k++)
		{
			fscanf(f1,"%d",&grid2[j][k]);
	     if(grid1[j][k]>16&&grid1[j][k]<1)
		{
			fclose(f1);
		     fclose(f2);
		     return 0;
			}
		}
	for(j=0;j<4;j++)
	for(k=0;k<4;k++)
		if(grid1[ans1-1][j]==grid2[ans2-1][k])
		{
		       *(ans+i)=*(ans+i)+1; *(found+i)=grid1[ans1-1][j];
		//	printf("%d\t%d\n",*(ans+i),*(found+i));
//			cout<<ans[i]<<"\t"<<found[i]<<endl;
	   }
}

for(i=0;i<t;i++)
{
	if(ans[i]==0)
		fprintf(f2,"Case #%d: Volunteer cheated!\n",(i+1));
	if(ans[i]==1)
		fprintf(f2,"Case #%d: %d\n",(i+1),*(found+i));
	if(ans[i]>1)
		fprintf(f2,"Case #%d: Bad magician!\n",(i+1));
}
/*
for(i=0;i<t;i++)
{
	if(ans[i]==0)
		printf("Case #%d: Volunteer cheated!\n",(i+1));
	if(ans[i]==1)
		printf("Case #%d: %d\n",(i+1),found[i]);
	if(ans[i]>1)
		printf("Case #%d: Bad magician!\n",(i+1));
}
*/

fclose(f1);
fclose(f2);
    system("PAUSE");
    return EXIT_SUCCESS;
}