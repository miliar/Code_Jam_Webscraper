#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<sstream>
using namespace std;
int cal(int n,int k){
	int ans=0;
	for(int i=0;i<k;i++)
		ans+=n-i;
	return ans;
}
bool check(int count[]){
	bool res=false;
	for(int i=0;i<1005;i++)
		res|=count[i];
	return res;
}
int main(){
	int C;
	scanf("%d",&C);
	for(int Case=1; Case<=C; Case++){
		int n,m;
		scanf("%d%d",&n,&m);
		int o[1005],e[1005],p[1005];
		int count[1005]={};
		int cost1=0,cost2=0;
		for(int i=0;i<m;i++){
			scanf("%d%d%d",&o[i],&e[i],&p[i]);
			for(int j=o[i];j<e[i];j++)
				count[j]+=p[i];
			cost1+=cal(n,e[i]-o[i])*p[i];
		}
		while(check(count)){
			/*for(int i=0;i<15;i++)
				printf("%d ",count[i]);
			puts("");*/
			for(int i=0;i<1005;i++)
				if(count[i]>0){
					int j=i+1;
					int min=count[i];
					for(;j<1005;j++){
						if(count[j]==0)
							break;
						if(count[j]<min)
							min=count[j];
					}
					cost2+=cal(n,j-i)*min;
					for(int k=i;k<j;k++)
						count[k]-=min;
					break;
				}
		}
		printf("Case #%d: %d\n",Case,cost1-cost2);
	}
}

