#include "stdio.h"
#include "string.h"
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int N,M;
const long long MM=1000002013;
int flow[105];
void Process(){
}
int price(int s){
	return (N+N-s+1)*s/2;
}
long long clean(){
	int min_index=0;
	for(int i=1;i<N-1;i++){
		if(flow[i]==0) continue;
		if((flow[min_index]==0)||(flow[i]<flow[min_index])) min_index=i;
	}
	if(flow[min_index]==0) return 0;
	int min_value=flow[min_index];
	long long total=0;
	while(1){
		//cout<<"while";
		if(min_index==0) break;
		if(flow[min_index-1]<min_value) break;
		min_index--;
	}
	int i;
	for(i=min_index;flow[i]>=min_value;i++){
		flow[i]-=min_value;
	}
	return min_value*price(i-min_index);
}
void Solve(){
	memset(flow,0,sizeof(flow));
	long long total=0;
	scanf("%d%d",&N,&M);
	for(int i=0;i<M;i++){
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		a--;
		b--;
		for(int j=a;j<b;j++)
			flow[j]+=c;
		total+=c*price(b-a);
		total%=MM;
		//cout<<"total"<<total<<endl;
	}
	//cout<<"total-end"<<total<<endl;
	long long total2=0;
	while(1){
		//cout<<"while2";
		long long more=clean();
		//cout<<"more"<<more<<endl;
		if(more==0) break;
		else total2+=more;
		total2%=MM;
	}
	//cout<<"total "<<total<<endl;
	//cout<<"total2 "<<total2<<endl;
	long long res=total-total2;
	if(res<0) res+=MM;
	printf("%lld\n",res);
}
int main(){
	//freopen("D:\\Test\\in.txt","r",stdin);
	//freopen("D:\\Test\\out.txt","w",stdout);
	freopen("D:\\VS Projects\\contests\\contests\\in.txt","r",stdin);
	freopen("D:\\VS Projects\\contests\\contests\\out.txt","w",stdout);
	Process();
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){			
		printf("Case #%d: ",t);
		Solve();
	}
    return 0;
}