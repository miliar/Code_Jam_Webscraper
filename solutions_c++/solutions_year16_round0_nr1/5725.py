#include<stdio.h>
#include<string.h>

using namespace std;
int main()
{

  char ch;

  int t;
  long long n,rnd,d;
  FILE * fin, * fot;
  fin = fopen ("largeA.in","r");
  fot = fopen ("ans.out","w");
  fscanf(fin,"%d",&t);

for(int i=0;i<t;i++)
{
  fscanf(fin,"%lld",&n);
  if(n==0)
  {
      fprintf(fot,"Case #%d: INSOMNIA\n",i+1);continue;
  }
  bool all[10];
  memset(all,false,sizeof all);
  int cnt=10;
  rnd=0;
  while(cnt>0)
  {
      rnd+=n;
      d=rnd;
      while(d)
      {
          if(!all[d%10])
          {
              all[d%10]=true;
              cnt--;
          }
          d/=10;
      }
  }
  fprintf(fot,"Case #%d: %lld\n",i+1,rnd);
}

  fclose(fin);
  fclose(fot);

}
