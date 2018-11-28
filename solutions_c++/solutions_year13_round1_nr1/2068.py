#include <stdio.h>
#include <iostream>
#include <math.h>

char input[100];
char a[100][100];
unsigned int  t;
unsigned int  r;
//long long  t;
//long long  r;
unsigned int ans;
unsigned int count = 0;

int main()
{
    //freopen("B-small-practice.in","r",stdin);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("AA.out","w",stdout);
    //freopen(".in","r",stdin);
    //freopen("x.out","w",stdout);
	int T;
	int i, j, k, n, m;

	scanf("%d ",&T);
	for (int test=1;test<=T;test++) {
     
		scanf("%lu %lu",&r,&t);
		//printf("r=%lu t=%lu\n",r,t);
      count = 0;
      ans = 0;
      r = r+1;
      while(ans <= t)
      {
         count++;
         ans = ans + ((r*r) - ((r-1)*(r-1)));  
         r = r+2;
         //printf("ans=%lu, count=%lu, r=%lu\n", ans,count,r);
      }
		//printf("%lu\n",count-1);
		//printf("%lu\n",ans);

		printf("Case #%d: %lu\n",test,count-1);
	}
}
