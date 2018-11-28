#include <cstdio>
//#include <fstream>
using namespace std;
int main()
{
  //ofstream fout("ans.txt");
  char filename[33];
  scanf("%s",filename);
  
  FILE *fpw,*fpr;
  fpw=fopen("ans.txt","w");
  fpr=fopen(filename,"r");
  
  int t,i;
  fscanf(fpr,"%d",&t);
  
  bool b[20];
  int i1,i2,x1,x2;
  int a1[5][5],a2[5][5];
  for(i=1;i<=t;i++)
  {
    fprintf(fpw,"Case #%d: ",i);
	
	for(i1=1;i1<=16;i1++)
	  b[i1]=false;
	fscanf(fpr,"%d",&x1);
	for(i1=1;i1<=4;i1++)
	  for(i2=1;i2<=4;i2++)
	  { 
		fscanf(fpr,"%d",&a1[i1][i2]);
		if(x1==i1)b[a1[i1][i2]]=true;
	  }
	fscanf(fpr,"%d",&x2);
	for(i1=1;i1<=4;i1++)
	  for(i2=1;i2<=4;i2++)
	  {
	    fscanf(fpr,"%d",&a2[i1][i2]);
		if(i1!=x2)b[a2[i1][i2]]=false;
	  }
	
	int num=0,ans;
	for(i1=1;i1<=16;i1++)
	  if(b[i1])
	  {
	    if(!num) ans=i1;
		num++;
	  }
	
	if(num==1)fprintf(fpw,"%d",ans);
	else if(num==0)fprintf(fpw,"Volunteer cheated!");
	else if(num>1)fprintf(fpw,"Bad magician!");
	
	if(i<t) fprintf(fpw,"\n");
  }
  //while(1);
  return 0;
}
