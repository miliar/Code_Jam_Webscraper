#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
	int t,smax;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&smax);		
		char c[smax+1],v;
		scanf("%c",&v);
		for(int j=0;j<=smax;j++){
			scanf("%c",&c[j]);
		}
		int stand=c[0]-48,extra=0;
		for(int j=1;j<=smax;j++){
			if(c[j]-48!=0){
				//cout<<j<<" stand:"<<stand<<":"<<c[j]-48<<endl;
				if(stand>=j){
					stand+=(c[j]-48);
				}
				else{
					extra+=j-stand;
					stand += (c[j]-48)+extra;
					
				}
			}
		}
		printf("Case #%d: %d\n",i,extra);
	}
	return 0;
}
