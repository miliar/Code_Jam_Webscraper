#include <cstdio>
#include <algorithm>
 
using namespace std;
 
int T,N,A[10005],ans;
 
int main(){
scanf("%d",&T);
for(int xx=1;xx<=T;++xx){
scanf("%d",&N);
ans=-1;
for(int i=0;i<N;++i) {
scanf("%d",&A[i]);
ans=max(ans,A[i]);
}

/*for(int i=0;i<=ans;++i){
int cnt=0;
for(int j=0;j<N;++j){
int zz=1;
while((A[j]>zz/2)&&(A[j]/zz+(A[j]%zz!=0)>i)){zz*=2;cnt++;}
}
ans=min(ans,cnt+i);
}*/

for(int i = 1; i <= ans; ++i){
	int cnt = 0;
	for(int j = 0; j < N; ++j){
		if(A[j] % i == 0) cnt += A[j] / i - 1;
		else cnt += A[j] / i;
	}
	ans = min(ans, cnt + i);
}

printf("Case #%d: %d\n",xx,ans);
}
}