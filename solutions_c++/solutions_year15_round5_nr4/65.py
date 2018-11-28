#include<stdio.h>
#include<algorithm>
#include<map>
using namespace std;
long long E[11000];
long long F[11000];
pair<long long ,long long>v[11000];
int now[110];
long long rem[11000];
map<int,int>h;
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a;scanf("%d",&a);
		for(int i=0;i<a;i++)scanf("%lld",E+i);
		for(int i=0;i<a;i++)scanf("%lld",F+i);
		for(int i=0;i<a;i++)v[i]=make_pair(E[i],F[i]);
		std::sort(v,v+a);
		now[0]=0;
		int sz=0;
		long long tt=0;
		for(int i=0;i<a;i++)tt+=F[i];
		while(tt>1){
			sz++;
			tt/=2;
		}
		h.clear();
		for(int i=0;i<a;i++)h[E[i]]=i;
		for(int i=0;i<sz;i++){
			for(int j=0;j<a;j++)rem[j]=F[j];
			for(int j=0;j<(1<<i);j++){
				long long ss=0;
				for(int k=0;k<i;k++)if(j&(1<<k))ss+=now[k];
				rem[h[ss]]--;
			}
			for(int j=0;j<a;j++){
				if(rem[h[v[j].first]]){
					now[i]=v[j].first;
					break;
				}
			}
		}
		printf("Case #%d:",t);
		for(int i=0;i<sz;i++)printf(" %d",now[i]);
		printf("\n");
	}
}