#include <cstdio>
#include <vector>

using namespace std;

const int maxn = 10000;
vector <int> primes;
vector <long long> resp;
vector <long long> div[12];
int ok2[maxn];

int mod(int val,int pot,int num){
	long long resp=1;
	for(int i=0;i<pot;i++){
		resp*=val;
		resp%=num;
	}
	return resp;
}

int ver[maxn];
int main(){
	int t;
	scanf("%d",&t);
	int n,qtd;
	scanf("%d %d",&n,&qtd);
	for(int i=2;i<10000;i++){
		if(ver[i]==0)primes.push_back(i);
		for(int j=i*i;j<10000;j+=i){
			ver[j]=1;
		}
	}
	int val=0;
	for(int i=0;i<(1<<(n-2));i++){
		int ok=1;
		for(int j=2;j<=10;j++){
			ok2[j]=0;
			for(int k=0;k<primes.size();k++){
				int at=mod(j,0,primes[k])+mod(j,n-1,primes[k]);
				for(int l=0;l<=n-2;l++){
					if(i&(1<<l)){
						at+= mod(j,l+1,primes[k]);
						at%=primes[k];
					}
				}
				if(at==0){
					ok2[j]=primes[k];
					break;
				}
			}
		}
		for(int j=2;j<=10;j++){
			if(ok2[j]==0)ok=0;
		}
		if(ok){
			val++;
			for(int j=2;j<=10;j++){
				div[j].push_back(ok2[j]);
			}
			resp.push_back(i*2+1+(1<<(n-1)));
		}
		if(val>=qtd)break;
	}

	printf("Case #1:\n");
	for(int i=0;i<qtd;i++){
		for(int j=n-1;j>=0;j--){
			if(resp[i]&(1<<j))printf("1");
			else printf("0");
		}
		printf(" ");
		int space=0;
		for(int j=2;j<=10;j++){
			if(space)printf(" ");
			printf("%lld",div[j][i]);
			space=1;
		}
		printf("\n");
	}
}