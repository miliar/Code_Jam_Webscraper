#include<string>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
using namespace std;
#define N 1010
float war_n[N],war_k[N];
bool visited[N];
void init(){
	for(int i=0;i<N;i++){
		war_n[i]=2.0;
		war_k[i]=2.0;
		visited[i]=false;
	}
}
bool comp(const float&p,const float & q){
	if(p>q)return true;
	return false;
}
int main(){
	freopen("d.in","r",stdin);
	freopen("a.out","w",stdout);
	int cases;
	cin>>cases;
	for(int t=1;t<=cases;t++){
		init();
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			cin>>war_n[i];
		for(int i=0;i<n;i++)
			cin>>war_k[i];
		sort(&war_n[0],&war_n[n]);
		sort(&war_k[0],&war_k[n]);
		
		int count_org=0;
		for(int i=0;i<n;i++){
			float naomi=war_n[i];
			int min=-1;
			for(int j=0;j<n;j++){
				if(!visited[j]&&war_k[j]>naomi){
					visited[j]=true;
					min=j;
					break;
				}
			}
			if(min==-1) count_org++;
		}
		int count_dec=0;
		sort(war_k,war_k+n,comp);
		memset(visited,0,sizeof(visited));
		for(int i=0;i<n;i++){
			float ken=war_k[i];
			int min=-1;
			for(int j=0;j<n;j++){
				if(!visited[j]&&war_n[j]>ken){
					visited[j]=true;
					min=j;
					break;
				}
			}
			if(min!=-1) count_dec++;
		}
		printf("Case #%d: %d %d\n",t,count_dec,count_org);
	}
}
