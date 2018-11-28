#include <cstdio>
using namespace std;
int n,a[1000005];
bool b[10];
bool f(){
	for(int i=0; i<10; ++i)
		if (!b[i]) return 0;
	return 1;
}
int main(){
	for(int i=1; i<=1000000; ++i){
		int t=i,cnt=0;
		for(int j=0; j<10; ++j) b[j]=0;
		while(!f()){
			++cnt;
			int t2=t*cnt;
			while(t2){
				b[t2%10]=1;
				t2/=10;
			}
		}
		a[i]=i*cnt;
	}
	scanf("%d",&n);
	for(int i=1; i<=n; ++i){
		int inp;
		scanf("%d",&inp);
		printf("Case #%d: ",i);
		if (inp==0) printf("INSOMNIA\n");
		else printf("%d\n",a[inp]);
	}
	return 0;
}
