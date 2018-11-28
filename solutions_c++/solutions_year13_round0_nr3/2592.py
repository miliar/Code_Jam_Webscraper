#include <cstdio>
#include <vector>

using namespace std;

int log10(long long n){
	int r;
	for (r=0;n>0;n/=10) r++;
	return r;
}

long long puiss(int e){
	long long res=1;
	for (;e>0;e--) res*=10;
	return res;
}

long long rev(long long n){
	long long r=0;
	for (;n>0;n/=10) r=r*10+n%10;
	return r;
}

bool palin(long long n){
	int c=log10(n);
	long long d=n%puiss(c/2),f=n/puiss((c+1)/2);
	return d==rev(f);
}

long long nb(long long n){
	int res=0;
	for (int i=1;i<10000;i++){
		if (i%10==0)
			continue;
		long long r=rev(i);
		long long p=r*puiss(log10(i))+i;
//		printf("%lld\n",p);
		if (p*p<=n && palin(p*p)){
//			printf("%lld %lld\n",p,p*p);
			res++;
		}
		p=(r/10)*puiss(log10(i))+i;
//		printf("%lld\n",p);
		if (p*p<=n && palin(p*p)){
//			printf("%lld %lld\n",p,p*p);
			res++;
		}
//		if (palin(i))
//			printf("%d\n",i);
	}
	return res;
}

void pb(){
	long long d,f;
	scanf("%lld%lld",&d,&f);
	printf("%lld\n",nb(f)-nb(d-1));
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		pb();
	}
	return 0;
}
