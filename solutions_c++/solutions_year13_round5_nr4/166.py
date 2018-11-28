#include <cstdio>
using namespace std;
static double dp[20][1<<20];
int main()
{
	for (int N=1;N<=20;N++){
		double * d=dp[N-1];
		d[0]=0;
		for (int i=1;i<(1<<N);i++){
			double s=0;
			for (int j=0;j<N;j++){
				int k=N;
				int p=j;
				while (((1<<p)&i)==0){
					k--;
					p=p+1;
					if (p==N)p=0;
				}
				s+=k+d[i^(1<<p)];
			}
			d[i]=s/N;
		}
	}
	int T;
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		printf("Case #%d: ",Case);
		char buf[1024];
		scanf("%s",buf);
		int N=0;
		while (buf[N])N++;
		int id=0;
		for (int i=0;i<N;i++)
			if (buf[i]=='.')
				id|=(1<<i);
		printf("%.20f\n",dp[N-1][id]);
	}
	return 0;
}

