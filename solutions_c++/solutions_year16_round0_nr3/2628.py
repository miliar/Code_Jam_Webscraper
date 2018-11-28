#include <cstdio>
#define N 1000000
#define LL long long
int a[N+13], p[N+13], pnum,b[13];
void print(LL x){
	if (x==0)return;
	print (x/2);
	printf("%lld",x&1);
}
int main(){
	pnum=0;
	for (int i=2;i<=N;i++){
		if (a[i]==0){
			p[pnum++]=i;
			for (int j=i+i;j<=N;j+=i)a[j]=1;
		}
	}
	int T;
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		int n,j;
		scanf("%d%d",&n,&j);
		printf("Case #%d:\n",Case);
		LL x = (1LL<<(n-1)) + 1LL;
		//printf("%lld %lld\n",x,1LL<<n);
		for (LL i = x;i<(1LL<<n) && j;i++){
			if ((i&1) ==0) continue;
			//printf(">> ");
			//print(i);
			bool ans=true;
			for (int y=2;y<=10;y++){
				b[y]=0;
				LL x2 = i;
				LL y2 = 1LL;
				LL z2 = 0LL;
				while (x2!=0){
					if (x2&1){
						z2+=y2;
					}
					x2/=2;
					y2*=y;
				}
				//printf(" %lld", z2);
				for (int q=0;q<pnum && p[q] < z2;q++){
					if (z2%p[q] ==0){
						b[y]=p[q];
						break;
					}
				}
				if (b[y]==0){ans=false;break;}
			}
			//printf("\n");
			if (ans && j){
				j--;
				print(i);
				for (int y=2;y<=10;y++){printf(" %d",b[y]);}printf("\n");
			}
		}
	}

	return 0;
}
