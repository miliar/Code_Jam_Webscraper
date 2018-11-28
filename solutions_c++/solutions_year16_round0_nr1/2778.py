#include<bits/stdc++.h>
using namespace std;

int main(){
	
	freopen("input.txt", "r" , stdin);
	freopen ("output.txt","w",stdout);
	
	int t,r,i,j,n;
	scanf("%d",&t);
	
	for(r=1;r<=t;++r){
		int mark[10]={0};
		scanf("%d",&n); int num=-1;
		printf("Case #%d: ",r);
		for(i=1;i<=1000;++i){
			if(n==0) break;
			int flag=1;
			int temp=n*i; num=temp;
			while(temp>0){
				int z=temp%10;
				mark[z]=1;
				temp=temp/10;
			}
			for(j=0;j<10;++j){
				if(mark[j]!=1) flag=0;
			}
			if(flag==1){
				break;
			} 
		}
		int ans=1;
		for(i=0;i<10;++i){
			if(mark[i]!=1) ans=0;
		}
		if(ans==0){
			printf("INSOMNIA\n");
		}
		else{
			printf("%d\n",num);
		}
	}
	
	fclose(stdout);
	return 0;
}
