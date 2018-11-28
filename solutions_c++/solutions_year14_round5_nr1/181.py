#include<stdio.h>
#include<algorithm>
using namespace std;
long long sum[1100000];
long long b[1100000];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int a;
		long long p,q,r,s;
		scanf("%d%lld%lld%lld%lld",&a,&p,&q,&r,&s);
		for(int i=0;i<a;i++){
			b[i]=(i*p+q)%r+s;
		}
		for(int i=0;i<a;i++)sum[i+1]=sum[i]+b[i];
		long long ret=0;
		for(int i=0;i<a;i++){
			long long left=sum[i];
			// L is biggest
			int at1=upper_bound(sum,sum+a+1,left+left)-sum-1;
			int at2=upper_bound(sum,sum+a+1,sum[at1]+left)-sum-1;
			if(at2>=a)ret=max(ret,sum[a]-left);
			// L is not biggest
			long long v=sum[a]-sum[i];
			int at3=upper_bound(sum,sum+a+1,left+v/2)-sum-1;
			for(int j=-3;j<=3;j++){
				if(at3+j<i||at3+j>a)continue;
				long long one=left;
				long long two=sum[at3+j]-sum[i];
				long long three=sum[a]-sum[at3+j];
				long long M=max(one,max(two,three));
				ret=max(ret,sum[a]-M);
			}
		}
		printf("Case #%d: %.12f\n",t+1,(double)ret/sum[a]);
	}
}