#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#define CL(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(e);i++)
#define x first
#define y second
#define MAX 10005
#define INF 1<<29
#define LL long long int

using namespace std;

int T,N,J;

LL isprime(LL n){
	for (LL i=2;i*i<=n;i++) if (n%i==0) return i;
	return 0;
}

int main(){
	scanf("%d%d%d",&T,&N,&J);
	printf("Case #1:\n");
	for (int i=(1<<15)+1,j=0;j<J;i++){
		if ((i&1)!=1) continue;
//		printf("%d\n",i);
//			for (int k=15;k>=0;k--) printf("%c",(i&(1<<k))?'1':'0');
//			puts("");
		bool ok = true;
		vector<LL> l;
		for (int b=2;b<=10;b++){
			LL v = 0;
			for (int k=15;k>=0;k--){
				v*=b;
				if (i&(1<<k)) v+=1;
			}/*
			int num = i,k=0;
			while (num>0){
				if (num%2==1) v+=pow(b,k);
				num/=2;
				k++;
			}*/
//			printf("i=%d v=%lld\n",i,v);
			LL f = isprime(v);
			if (f==0) {
				ok=false;
				break;	
			}
			l.pb(f);
		}
		if (ok) {
			for (int k=15;k>=0;k--) printf("%c",(i&(1<<k))?'1':'0');
			for (LL x:l) printf(" %lld",x);
			puts("");
			j++;
		}
	}
}
