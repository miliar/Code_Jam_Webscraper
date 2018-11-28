#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
  char filename[33];
  scanf("%s",filename);
  FILE *fr,*fw;
  fr=fopen(filename,"r");
  fw=fopen("ans.txt","w");
  
  int t,i;
  fscanf(fr,"%d",&t);
  for(i=1;i<=t;i++)
  {
    fprintf(fw,"Case #%d: ",i);
	
	double naomi[1003],ken[1003];
	int num;
	fscanf(fr,"%d",&num);
	int i1,i2,i3;
	for(i1=1;i1<=num;i1++)
	  fscanf(fr,"%lf",&naomi[i1]);
	for(i1=1;i1<=num;i1++)
	  fscanf(fr,"%lf",&ken[i1]);
	sort(naomi+1,naomi+num+1);
	sort(ken+1,ken+num+1);
	
	int ans_orin,ans_cheat,pn,pk;
	ans_orin=ans_cheat=0;
	pn=pk=num;
	
	//printf("num=%d\n",num);
	
	while(pn&&pk)
	{
	  while(pn&&pk&&ken[pk]>naomi[pn])
	  {
	    pk--;pn--;ans_orin++;
	  }
	  while(pn&&pk&&ken[pk]<naomi[pn])pn--;
	}
	pn=pk=num;
	while(pn&&pk)
	{
	  while(pn&&pk&&naomi[pn]>ken[pk])
	  {
	    pk--;pn--;ans_cheat++;
	  }
	  while(pn&&pk&&naomi[pn]<ken[pk])pk--;
	}
    fprintf(fw,"%d %d",ans_cheat,num-ans_orin);
	if(i<t) fprintf(fw,"\n");
  }
  
  //while(1);
  return 0;
}
