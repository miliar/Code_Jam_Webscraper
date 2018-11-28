#include<stdio.h>
#include<algorithm>
using namespace std;
int bit[131072];
int sum(int a,int b){
	if(a)return sum(0,b)-sum(0,a-1);
	int ret=0;
	for(;b>=0;b=(b&(b+1))-1)ret+=bit[b];
	return ret;
}
void add(int a,int b){
	for(;a<131072;a|=a+1)bit[a]+=b;
}
int b[110000];
pair<int,int> c[110000];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int a;scanf("%d",&a);
		for(int i=0;i<a;i++)scanf("%d",b+i);
		for(int i=0;i<a;i++)c[i]=make_pair(b[i],i);
		std::sort(c,c+a);
		for(int i=0;i<a;i++)add(i,1);
		int at=0;
		long long ret=0;
		for(int i=0;i<a;i++){
			while(at<a&&c[at].first==c[i].first){
				add(c[at].second,-1);
				at++;
			}
			ret+=min(sum(0,c[i].second),sum(c[i].second,131071));
		}
		printf("Case #%d: %lld\n",t+1,ret);
	}
}