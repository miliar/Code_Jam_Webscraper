#include<cstdio>
#include<cstdlib>
#include<cstring>
#define LEN 1005
#define STR 10

int nt;
int a[LEN];
int b[LEN];
int Nwin,Dwin;

int calnum(char *w)
{
  int flen=strlen(w)-2;
  int i=0,temp=0;
  while(i<flen){
    temp*=10;
    temp=temp+(w[i+2]-'0');
    ++i;
  }
  while(i<5){
    temp*=10;
    ++i;
  }
  return temp;
}

int icmp(const void *p,const void *q)
{
  int *a=(int*)p;
  int *b=(int*)q;
  return (*a)-(*b);
}

void normalWar()
{
  Nwin=0;
  int i=0,j=0;
  while(i<nt&&j<nt){
    if(b[j]>a[i]){
      ++i;++j;
      ++Nwin;
    }else if(b[j]<a[i]){
      ++j;
    }
  }
  Nwin=nt-Nwin;
}

void deceitWar()
{
  Dwin=0;
  int i=0,j=0;
  while(i<nt&&j<nt){
    if(a[j]>b[i]){
      ++i;++j;
      ++Dwin;
    }else if(a[j]<b[i]){
      ++j;
    }
  }
}

int main(void)
{
  int tt;
  scanf("%d",&tt);
  for(int tc=1;tc<=tt;++tc){
    scanf("%d",&nt);
    for(int nc=0;nc<nt;++nc){
      char num[STR];
      scanf("%s",num);
      a[nc]=calnum(num);
      //printf(" %d",a[nc]);
    }
    //putchar('\n');
    for(int nc=0;nc<nt;++nc){
      char num[STR];
      scanf("%s",num);
      b[nc]=calnum(num);
      //printf(" %d",b[nc]);
    }
    //putchar('\n');
    qsort(a,nt,sizeof(a[0]),icmp);
    qsort(b,nt,sizeof(b[0]),icmp);
    normalWar();
    deceitWar();
    printf("Case #%d: %d %d\n",tc,Dwin,Nwin);
  }
  return 0;
}
