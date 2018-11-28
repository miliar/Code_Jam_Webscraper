#include <cstdio>
using namespace std;

double binom[3000][3000];//


int main(){
	int t;
	scanf("%d",&t);
	binom[0][0]=1;
	for(int i=1;i<3000;i++){
		binom[i][0]=binom[i-1][0]/2;
		binom[i][i]=binom[i-1][i-1]/2;
		for(int j=1;j<i;j++){
			binom[i][j]=(binom[i-1][j]+binom[i-1][j-1])/2;
		}
	}
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		int n,x,y;
		scanf("%d %d %d",&n,&x,&y);
		int k=0;
		for(int i=2;;i++){
			if(i*(2*i-1)>n){
				k=i-1;
				break;
			}
		}
		n-=k*(2*k-1);
		if(x<0)x=-x;
		double prob;
		if(x+y<=2*k-2){
			prob=1;
		}else if(x+y>2*k||x==0){
			prob=0;
		}else if(2*k+y+1<=n){
			prob=1;
		}else{
			prob=0;
			for(int i=y+1;i<=n;i++){
				prob+=binom[n][i];
			}
		}
		printf("%lf\n",prob);
	}

}
