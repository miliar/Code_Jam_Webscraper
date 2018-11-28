#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <vector>

using namespace std;

#define LL long long

#define NMAX_JC (1<<14)

LL jcs[NMAX_JC][9];
int jc_prime[NMAX_JC][9];
int jc_naccept[NMAX_JC];

vector<int> primes;

void get_primes(void)
{
	const int prime_max = 1<<16;
	char flag[prime_max+1];
	memset(flag,0,sizeof(flag));
	for (int i=2;i<=prime_max;i++){
		if (flag[i]==0){
			primes.push_back(i);
			int j=i;
			while (1){
				flag[j]=1;
				j+=i;
				if (j>prime_max)break;
			}
		}
	}
	/*for (unsigned int i=0;i<primes.size();i++){
		printf("%d ",primes[i]);
	}
	printf("\n");*/
}

void print_ret(int jc_idx)
{
	printf("%lld ",jcs[jc_idx][8]);
	for (int i=0;i<9;i++){
		printf("%d",jc_prime[jc_idx][i]);
		if (i!=8)printf(" ");
	}
	printf("\n");
}

int main(int argc,char **argv)
{
	get_primes();
	int T;
	scanf("%d\n",&T);
	for (int t=1;t<=T;t++){
		memset(jcs,0,sizeof(jcs));
		memset(jc_prime,0,sizeof(jc_prime));
		memset(jc_naccept,0,sizeof(jc_naccept));
		int N,J;
		scanf("%d %d\n",&N,&J);
		int jc_base = 1<<(N-1) | 1;
		int n_jc = 0;
		while (1){
			//printf("%d ",jc_base);
			for (int i=0;i<=8;i++){
				LL jc = 0;
				int jctmp = jc_base;
				for (int j=0;j<N;j++){
					//printf("%d %lld\n",jctmp,jc);
					jc *= i+2; // 2-10
					if (jctmp & (1<<(N-1)) ){
						jc += 1;
					}
					jctmp = jctmp << 1;
				}
				jcs[n_jc][i]=jc;
				//printf("%lld ",jc);
			}
			//printf("\n");
			n_jc++;
			if (jc_base == ((1<<N)-1))break;
			jc_base+=2;
		}
		assert(n_jc == 1<<(N-2));
		printf("Case #%d:\n",t);
		int jc_ok_count=0;
		for (unsigned int i=0;i<primes.size();i++){
			//printf("%d ",primes[i]);
			for (int j=0;j<n_jc;j++){
				for (int k=0;k<9;k++){
					if (jcs[j][k]<=primes[i])continue;
					if (jcs[j][k]%primes[i]==0){
						if (jc_prime[j][k]==0){
							//printf("%lld %d\n",jcs[j][k],primes[i]);
							jc_prime[j][k]=primes[i];
							jc_naccept[j]++;
							if (jc_naccept[j]==9){
								print_ret(j);
								jc_ok_count++;
								if (jc_ok_count==J)return 0;
							}
						}
					}
				}
			}
		}
	}
	return 0;
}
