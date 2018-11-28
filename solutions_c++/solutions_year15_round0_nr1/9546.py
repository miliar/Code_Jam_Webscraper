#include<stdio.h>


using namespace std;
int main()
{

  char ch;

  int t,smax,ps,ans;
  FILE * fin, * fot;
  fin = fopen ("biga.in","r");
  fot = fopen ("ans.out","w");
  fscanf(fin,"%d",&t);

for(int i=0;i<t;i++)
{
  fscanf(fin,"%d",&smax);
  char c[smax+5];
  int temp;
  fscanf(fin,"%s",c);
  ps=0;ans=0;
 // printf("Case %d : %d  %s\n",i+1,smax,c);
  for(int j=0;j<=smax;j++){
      //printf("%dmun temp:%d, ps:%d, ans:%d\n",j,temp,ps,ans);
     temp=c[j]-48;
     if(j<=ps)
        ps+=temp;
     else
        if(temp>0)
          {
              ans+=(j-ps);
              ps=j;
              ps+=temp;
          }
     //printf("%dpin temp:%d,ps:%d,ans:%d\n",j,temp,ps,ans);
  }
  fprintf(fot,"Case #%d: %d\n",i+1,ans);
}

  fclose(fin);
  fclose(fot);

}
