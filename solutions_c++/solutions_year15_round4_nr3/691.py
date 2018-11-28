#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#define REP(I,A,B) for (int I=A,END=B;I<=END;I++)
#define REPD(I,A,B) for (int I=A,END=B;I>=END;I--)
#define RI(X) scanf("%d",&X)
#define RS(X) scanf("%s",X)
#define RD(X) scanf("%lf",&X)
#define RLL(X) scanf("%I64d",&X)
#define GCH getchar()
#define PCH(X) putchar(X)
#define MS(X,Y) memset(X,Y,sizeof(X))
#define MC(X,Y,var,len) memcpy(X,Y,sizeof(var)*(len))
#define debug(...) fprintf(stderr,__VA_ARGS__)
using namespace std;

const int MAXN = 2;

struct source
{
  double r;
  double c;
}s[MAXN]={0};

double v,x;
double t;

const double eps=1e-7;

void open()
{
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
}
void close()
{
  fclose(stdin);
  fclose(stdout);
}

int dcmp(const int &a)
{
  if (fabs(a)<=eps)
    return 0;
  else if (a>eps)
    return 1;
  else 
    return -1;
}

void init()
{
}
//只有两支水源  R1*t*v1+R2     
int main()
{
  open();
  int _=0;
  RI(_);
  REP(__,1,_)
  {
    init();
  }
  close();
  return 0;
}

