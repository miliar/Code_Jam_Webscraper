#include <cstdio>
using namespace std;
int main()
{
  char filename[33];
  FILE *fr,*fw;
  scanf("%s",filename);
  fr=fopen(filename,"r");
  fw=fopen("ans.txt","w");
  
  int t,i;
  fscanf(fr,"%d",&t);
  for(i=1;i<=t;i++)
  {
    fprintf(fw,"Case #%d: ",i);
	
	double c,f,x;
	fscanf(fr,"%lf%lf%lf",&c,&f,&x);
	//c农场价格，f农场产能，x目标
	double ans=99999,tfarm=c/2.0,ttry=x/2.0,speed=2,time=0;
	
	//printf("%.1f %.1f %.1f ",c,f,x);
	
	while(ans>ttry)
	{
	  ans=ttry;
	  time+=tfarm;
	  speed+=f;
	  tfarm=c/1.0/speed;
	  ttry=time+x/1.0/speed;
	}
    fprintf(fw,"%.7f",ans);
	if(i<t) fprintf(fw,"\n");
  }
  //while(1);
  return 0;
}
