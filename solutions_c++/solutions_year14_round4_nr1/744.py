#include<cstdio>
#include<algorithm>
using namespace std;
int mem[10000];
int main(){
	int t;
	freopen("A-large.in","rt",stdin);
	freopen("A.out","wt",stdout);
	scanf("%d",&t);
	for(int _=1;_<=t;_++){
		printf("Case #%d: ",_);
		int n, x;
		scanf("%d %d",&n,&x);
		for(int i=0;i<n;i++) scanf("%d",mem+i);
		sort(mem,mem+n);
		int fr=0;
		int re=n-1;
		int res=0;
		while(fr<re){
			if(mem[fr]+mem[re]>x){
				re--;
				res++;
			}else{
				fr++,re--;
				res++;
			}
		}
		if(fr==re){
			res+=1;
		}
		printf("%d\n",res);
	}
}