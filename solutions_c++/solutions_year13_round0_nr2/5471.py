#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

long long int n,x,y,t;
long long int l1,l2,l3,l4;
long long num,c;

int main()
{
    scanf("%I64d%I64d%I64d%I64d",&n,&x,&y,&c);
    num=1;
    l1=l3=x;l2=l4=y;
    while (num<c)
    {
          t++;
          num+=4*t;
          l1--,l2--;l3++,l4++;
          if (l2<1) num-=(1-l2)*2-1;
          if (l1<1) num-=(1-l1)*2-1;
          if (l3>n) num-=(l3-n)*2-1;
          if (l4>n) num-=(l4-n)*2-1;
          if (l3-n-y>0) num+=(l3-n-y);
          if (t>n-x+n-y+1) num+=(t-(n-x+n-y+1));
		  if (l4-n-x>0) num+=(l4-n-x);
          if (t>x-1+y) num+=t-(x-1+y);
    }
    printf("%I64d\n",t);
    return 0;
}
