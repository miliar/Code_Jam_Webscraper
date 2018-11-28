#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
//#define LOCAL
typedef unsigned int uint;
const int N = 50;
int s[N],n,m;
int b[N];
const int NN = 7;
int a[NN]={3,5,7,11,13,17,19};

void tobit(uint n){
	for(int i=0;i<32;i++){
		s[i] = n&1;
		n>>=1;
	}
}
int check(int x){
	tobit(x);
	for(int i=2;i<=10;i++)
	{
		int flg=1;
		for(int k=0;k<NN;k++){
			int sum,q;
			sum=0;q=1;
			for(int j=0;j<n;j++){
				sum+=s[j]*q;
				q=(q*i)%a[k];
				sum%=a[k];
			}
			if (sum==0) {
				flg=0;
				b[i] = a[k];
				break;
			}
		}
		if (flg) return 0;
	}
	return 1;
}

void print(){
	for(int i=n-1;i>=0;i--) printf("%d",s[i]);
	for(int i=2;i<=10;i++) printf(" %d",b[i]);
	puts("");
}

int main(){
	#ifdef LOCAL
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int T;
	n = 32;
	scanf("%d",&T);
	for(int times=1;times<=T;times++){
		scanf("%d%d",&n,&m);
		int start=(1<<(n-1))|1;
		printf("Case #%d:\n",times);
		int j = start;
		for(int i=1;i<=m;i++){
			for(j+=2;;j+=2){
				if (check(j)){
					print();
					break;
				}
			}
		}
	}
	return 0;
}
