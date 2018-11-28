#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define rep(i,n) for(i = 0; i < n; ++i)

int isPalin(int n)
{
	if(n<10)
		return 1;
	if(n<100)
		return (n/10 == n%10);
	if(n<1000)
		return (n/100 == n%10);
	return 0;
}

int main(int argc,char **argv)
{
	int t,a,b,i,rt,j,cnt;
	FILE *in  = fopen(argv[1],"r");
	FILE *out = fopen("abc.txt","w");
	fscanf(in,"%d",&t);
	if(t < 1 || t > 100)
		return 0;
	rep(i,t){
		cnt=0;
		fscanf(in,"%d %d",&a,&b);
		for(j=a;j<=b;++j){
			if(j>9){
				if(!isPalin(j))
					continue;
			}
			rt = (int)sqrt((double)j);
			if(rt *rt == j && isPalin(rt))
				cnt++;
		}
		fprintf(out,"Case #%d: %d\n",i+1,cnt);
	}
	return 0;
}



