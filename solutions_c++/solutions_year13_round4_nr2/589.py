#include <cstdio>
#include <algorithm>
using namespace std;

int T;
long long N,P;

long long ans_y,ans_z;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	scanf("%d",&T);
	for(int _i=1;_i<=T;_i++){
		scanf("%lld %lld",&N,&P);
		
		// find_z
		ans_z = 0;
		long long val = 1;
		for(int i=1;i<=N-1;i++) val *= 2;
		for(long long i=2;i<=P;i*=2,val/=2) ans_z += val;
		
		val = 1;
		for(int i=1;i<=N-1;i++) val *= 2;
		//printf("P = %lld val = %lld\n",P,val+val);
		if(P == val*2) ans_z = P-1;
		
		// find_y
		ans_y = 0;
		long long left=0,right=1,mid;
		for(int i=1;i<=N;i++) right *= 2;
		
		//printf("[%lld,%lld]\n",left,right);
		long long val2 = 2;
		for(int i=1;i<=N;i++){
			mid = (left+right)/2;
			if(P>mid){
				ans_y += val2;
				left = mid;
				val2 *= 2;
			}else{
				//printf("val2 = %lld\n",val2);
				break;
			}
		}
		
		if(P == val*2) ans_y = P-1;
		
		printf("Case #%d: %lld %lld\n",_i,ans_y,ans_z);
	}
	return 0;
}