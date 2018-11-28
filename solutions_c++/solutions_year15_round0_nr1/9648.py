#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main(){
	int cas,t;
	int maxshy;
	int i;
	int add,sum;
	char listshy[1005];
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	cas=0;
	while(t--){
		scanf("%d",&maxshy);
		add=0;
		sum=0;
		scanf("%s",listshy);
		for(i=0;i<=maxshy;i++){
			if(sum<i){
				add+=(i-sum);
				sum=i;
			}
			sum+=(listshy[i]-'0');
			
		}
		printf("Case #%d: %d\n",++cas,add);
		
	}
	
}
