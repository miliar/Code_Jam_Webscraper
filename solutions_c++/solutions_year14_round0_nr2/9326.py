#include<stdio.h>
#include<conio.h>
#include<fstream.h>
#include<io.h>

void main()
{
clrscr();
FILE *fp1,*fp2;
fp1=fopen("fuck1.txt","r");
fp2=fopen("out.txt","w");
int tot;
fscanf(fp1,"%d",&tot);
int loopno=1;
for(loopno=1;loopno<=tot;loopno++){
fprintf(fp2,"Case #%d: ",loopno);
long float c1,p,x;
fscanf(fp1,"%lf %lf %lf",&c1,&p,&x);
//algorithm
long float time=0,b=2,nowtime=0,nexttime=0;
int i=0;
nowtime=time+(x/b);nexttime=time+(c1/b)+(x/(b+p));
while(nowtime>nexttime){
time=time+(c1/b);
b=b+p;
nowtime=time+(x/b);nexttime=time+(c1/b)+(x/(b+p));
i=i+1;}

time=nowtime;

fprintf(fp2,"%lf\n",time);
}
getch();
}